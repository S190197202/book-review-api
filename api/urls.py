from django.urls import path
from .views import (
    RegisterView, ChangePasswordView,
    BookListCreateView, BookDetailView,
    AddReviewView, BookReviewListView, ReviewDetailView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # 🔹 Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 🔹 Book endpoints
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # 🔹 Review endpoints
    path('books/<int:book_id>/reviews/', AddReviewView.as_view(), name='add-review'),
    path('books/<int:book_id>/reviews/list/', BookReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
