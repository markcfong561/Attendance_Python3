"""Attendance_Test URL Configuration

The `urlpatterns` list routes URLs to Attendance. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function Attendance
    1. Add an import:  from my_app import Attendance
    2. Add a URL to urlpatterns:  path('', Attendance.home, name='home')
Class-based Attendance
    1. Add an import:  from other_app.Attendance import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import Attendance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signIn', Attendance.signIn),
    path('signOut', Attendance.signOut),
    path('postsign', Attendance.postsign),
    path('postsign_signOut', Attendance.postsign_signOut)
]
