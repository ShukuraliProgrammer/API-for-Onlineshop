from rest_framework import generics
from accounts.api.v1.serializers import UserSerializer, ProfileSerializer, AddressSerializer
from accounts.models import BaseUser, Profile, Address
from rest_framework.permissions import IsAuthenticated


# from django.db import transaction

class CreateUserView(generics.CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = UserSerializer

    # @transaction.atomic
    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     profile = Profile.objects.create(
    #         user=user,
    #         name='',
    #         photo='',
    #         phone='',
    #         description='',
    #         gender='',
    #         birth_date='',
    #     )
    #
    #     cart = Cart.objects.create(
    #         profile=profile,
    #         completed=True,
    #     )


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
