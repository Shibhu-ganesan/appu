from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('user/', views.userpage, name="userpage"),
    path('account/', views.accountSettings, name="account"),
    path('register/', views.register, name="register"),
    path('login/', views.Login, name="login"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('products/', views.products, name="products"),
    path('createorder/<str:pk>', views.createOrder, name='createorder'),
    path('createcustomer/', views.createCustomer, name='createcustomer'),
    path('updatecustomer/<str:pk>', views.updateCustomer, name='updatecustomer'),
    path('updateorder/<str:pk>', views.updateOrder, name='updateorder'),
    path('deleteorder/<str:pk>', views.deleteOrder, name='deleteorder'),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('reset_password',
         auth_views.PasswordResetView.as_view(template_name="Account/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name="Account/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='Account/password_reset_form.html'),
         name="password_reset_confirm"),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="Account/password_reset_done.html"),
         name="password_reset_complete"),
]
