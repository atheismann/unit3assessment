from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add/', views.WishCreate.as_view(), name="add_wish"),
  path('<int:pk>/delete/', views.WishDelete.as_view(), name="delete_wish"),
  path('<int:pk>/edit/', views.WishUpdate.as_view(), name="edit_wish"),
]