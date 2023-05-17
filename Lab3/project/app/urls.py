"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='Список профилей'),
    path('profiles/<int:profile_id>/', views.ProfileDetails.as_view(), name='Профиль'),

    path('movies/', views.MovieList.as_view(), name='Список фильмов'),
    path('movies/<int:movie_id>/', views.MovieDetails.as_view(), name='Фильм'),

    path('purchases/', views.PurchaseList.as_view(), name='Список покупок'),
    path('purchases/<int:purchase_id>/', views.PurchaseDetails.as_view(), name='Покупка'),
]