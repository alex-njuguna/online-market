from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("/<int:pk>/", views.detail, name="detail"),
    
    path("/new/", views.new_item, name="new_item"),
    
    path("/<int:pk>/delete/", views.delete, name="delete"),
    
    path("/<int:pk>/update/", views.update, name="update"),
    
]
