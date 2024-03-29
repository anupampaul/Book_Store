from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('store_book/', views.store_book, name='store_book'),
    path('show_book/', views.show_book, name='show_book'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
]