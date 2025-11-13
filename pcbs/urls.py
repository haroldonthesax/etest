from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('board/<int:pk>', views.board, name='board'), # Created path to show each indinvidual board. 
    path('delete/<int:pk>', views.delete_board, name='delete_board'),
    path('add_board', views.add_board, name='add_board'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

]