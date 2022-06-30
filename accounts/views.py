from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import UserProfile
from accounts import mixins


class UserListCreateView(mixins.BaseUserViewMixin,
                         generics.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to register like john, justin etc person account
    or to see all user lists. register api also open for Non-Authenticated user
    and Only Authenticated admin super will be able to see user lists.<br/>
    when an admin user try to send this request:
    <ul>
        <li> It performs register operation after sending a post request </li>
        <li> It gives a list of user after sending a get request.</li>
    </ul>
    </div>
    """

    def list(self, *args, **kwargs):
        message = "Non-Authenticated users can't access it."
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return super().list(*args, **kwargs)
            message = "The user must be an admin to get all user data."
        return Response({"error": message}, status.HTTP_400_BAD_REQUEST)


class UserUpdateDeleteDestroyView(mixins.BaseUserViewMixin,
                                  generics.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for user crud operation.
    it is only for Authenticated users. <br/>Non-Authenticated users can't access it.
    when an admin user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the user details after sending a get request.</li>
    </ul>
    </div>
    """

    permission_classes = [IsAuthenticated, ]


class UserProfileCreateView(mixins.BaseUserProfileViewMixin,
                            generics.CreateAPIView):
    """
    <div style='text-align: justify;'>
    It is used to create the profile of an authenticated user.
    when an user try to send this request:
    <ul>
        <li> It performs create operation after sending a post request </li>
    </ul>
    </div>
    """

    def perform_create(self, serializer):
        if not hasattr(self.request.user, "profile"):
            serializer.save(user=self.request.user)
        return Response({"error": "This user profile already exist."}, status.HTTP_400_BAD_REQUEST)


class UserProfileUpdateDeleteDestroyView(mixins.BaseUserProfileViewMixin,
                                         generics.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for user crud operation.
    it is only for Authenticated users. Non-Authenticated users can't access it.
    when an user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the user profile details after sending a get request.</li>
    </ul>
    </div>
    """

    def get_object(self):
        return self.request.user.profile if hasattr(self.request.user, "profile") \
            else UserProfile.objects.create(user=self.request.user)

