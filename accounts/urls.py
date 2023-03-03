from django.urls import path
from accounts.views import (
    UserUpdateDeleteDestroyView,
    UserListCreateView,
    UserProfileCreateView,
    UserProfileUpdateDeleteDestroyView,
    LogoutView,
    LogoutAllView,
)

urlpatterns = [
    #  This URL is used for user registration and to see user lists
    path('user/', UserListCreateView.as_view(), name='create_list'),
    # This URL is used for a user to retrieve, partially or fully update and delete
    path('user/<int:pk>/', UserUpdateDeleteDestroyView.as_view(),
         name='user_retrieve_update_delete'),
    #  This URL is used for user registration and to see user lists
    path('user/profile/create/', UserProfileCreateView.as_view(), name='profile_create'),
    # This URL is used for a user to retrieve, partially or fully update and delete
    path('user/profile/', UserProfileUpdateDeleteDestroyView.as_view(),
         name='user_profile_retrieve_update_delete'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]
