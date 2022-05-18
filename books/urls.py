from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.Usersignup, name="Usersignup"),
    path("user_login/", views.User_login, name="User_login"),
    path("logout/", views.Logout, name="Logout"),
    path("for_users/", views.Users, name="Users"),
    path("checkout/", views.checkout, name="checkout"),
    path("bookcrossing/", views.book_crossing, name="bookcrossing"),
    path("see_bookcrossing/", views.see_requested_books, name="see_bookcrossing"),
    path("checkout/", views.checkout, name="checkout"),
]
