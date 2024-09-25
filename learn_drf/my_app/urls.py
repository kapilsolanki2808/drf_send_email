from . views import *


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('user/list/',ListUsers.as_view()),
    path('post/book/',PostBook.as_view()),
    path('verify/otp/',VerifyOTP.as_view()),
]
