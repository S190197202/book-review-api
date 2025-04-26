from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

from .models import Book, Review
from .serializers import (
    BookSerializer, ReviewSerializer,
    RegisterSerializer, ChangePasswordSerializer
)

# 🔹 تسجيل مستخدم جديد
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# 🔹 تغيير كلمة المرور
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "كلمة المرور الحالية غير صحيحة"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            update_session_auth_hash(request, user)
            return Response({"detail": "تم تغيير كلمة المرور بنجاح"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🔹 عرض جميع الكتب (وإضافة كتاب - للأدمن فقط)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [permissions.AllowAny()]


# 🔹 عرض تفاصيل كتاب وتعديله/حذفه (أدمن فقط للتعديل والحذف)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return [permissions.AllowAny()]


# 🔹 إضافة مراجعة لكتاب
class AddReviewView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_id = self.kwargs['book_id']
        serializer.save(user=self.request.user, book=Book.objects.get(id=book_id))


# 🔹 عرض كل المراجعات لكتاب معين
class BookReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book__id=book_id)


# 🔹 تعديل أو حذف مراجعة (صاحب المراجعة فقط)
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            return Response({"error": "غير مصرح لك بحذف هذه المراجعة"}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            return Response({"error": "غير مصرح لك بتعديل هذه المراجعة"}, status=status.HTTP_403_FORBIDDEN)
        return super().put(request, *args, **kwargs)

