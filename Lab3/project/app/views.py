# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        query = request.query_params.get('email')
        if query:
            queryset = queryset.filter(email__icontains=query)

        serializer = ProfileDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_url_kwarg = 'profile_id'

    def get(self, request, *args, **kwargs):
        profile_id = self.kwargs.get('profile_id')
        queryset = self.get_queryset().filter(id=profile_id)
        serializer = ProfileDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateOrUpdateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        query = request.query_params.get('name')
        if query:
            queryset = queryset.filter(name__icontains=query)

        serializer = MovieDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateOrUpdateSerializer
    lookup_url_kwarg = 'movie_id'

    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs.get('movie_id')
        queryset = self.get_queryset().filter(id=movie_id)
        serializer = MovieDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PurchaseDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class PurchaseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseUpdateSerializer
    lookup_url_kwarg = 'purchase_id'

    def get(self, request, *args, **kwargs):
        purchase_id = self.kwargs.get('purchase_id')
        queryset = self.get_queryset().filter(id=purchase_id)
        serializer = PurchaseDetailsSerializer(queryset, many=True)
        return Response(serializer.data)
