from django.contrib import admin
from django.urls import path
from crud_operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.receipe),
    path('update_receipe/<id>', views.update_recipe, name='update_receipe'),
    path('delete_receipe/<id>', views.delete_recipe, name='delete_receipe'),
]
