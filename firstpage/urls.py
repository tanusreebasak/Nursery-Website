from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),    
    path('cart/', views.cart,name="cart"),
    path('check-out/', views.checkout,name="check-out"),
    path('orders/', views.orders,name="orders"),
    path('plants/', views.plants,name="plants"),
    path('customer/<str:pk>', views.customer,name="customer"),
    path('create_order/<str:pk>/', views.createOrder,name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder,name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder,name="delete_order"),
    path('register/', views.registerPage , name="register"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutUser , name="logout"),    
    path('account/', views.accountSettings , name="account"),
] 