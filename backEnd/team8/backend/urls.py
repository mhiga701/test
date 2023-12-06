from django.urls import path
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib import admin
#from django.conf.urls import url 
#from core.views import * #not sure
from . import views
from .views import get_recipes, get_news, submit_rating, ReactView



urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('get_recipes/', views.get_recipes, name='get_recipes'),  # without parameter
    path('get_recipes/<str:ingredients>/', views.get_recipes, name='get_recipes_with_ingredients'),  # with parameter
    path('get_news/', get_news, name='get_news'),
    #path('rate_product/<int:recipe_id>/', rate_product, name='rate_product'), rating system
    path('submit_rating/<int:recipe_id>/', views.rate_recipe, name='rate_recipe'),

]
