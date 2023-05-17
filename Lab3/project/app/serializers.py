from rest_framework import serializers
from .models import Profile, Movie, Purchase


class ProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email', 'registration_date')


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'password')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('password',)


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'price')


class MovieCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'price')


class PurchaseDetailsSerializer(serializers.ModelSerializer):
    profile = ProfileDetailsSerializer()
    movie = MovieDetailsSerializer()

    class Meta:
        model = Purchase
        fields = ('id', 'profile', 'movie', 'purchase_date', 'rating')


class PurchaseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('profile', 'movie')


class PurchaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('rating',)
