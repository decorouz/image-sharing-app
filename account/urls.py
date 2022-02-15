from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # previous login view
    # path("login/", views.user_login, name="login"),

    # Djanog built-in authentication urls
    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Register user urls
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),

    # account activation auth
    path('account_activation_sent/', views.account_activation_sent,
         name='account_activation_sent'),
    path('activate/<uidb64>/<token>/',
         views.activate, name='activate'),

    # change password urls
    path("password_change/", auth_views.PasswordChangeView.as_view(),
         name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),

    # Reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # Account views
    path("", views.dashboard, name="dashboard"),

    # User list and details url
    path("users/", views.user_list, name="user_list"),
    path("users/<username>/", views.user_detail, name="user_detail"),




]
