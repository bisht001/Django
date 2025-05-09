from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.signup_view,name="signup_page"),
    path('login/',views.login_view,name="login_page"),
    path('logout/',views.logout_view,name="logout_page"),
]

# You can access these URLs by their names. 
# For example, if you want to redirect to the signup page, 
# you don't need to hardcode the URL path — just use the name 'signup_page'.