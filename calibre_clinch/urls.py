"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('instruction/',views.instruction),
    path('login/',views.login),
    path('mentorship/',views.mentorship),
    path('brainoregister/',views.brainoregister),
    path('dashboard/',views.dashboard),
    path('login1/',views.login1),
    path('home/', views.home, name='home'),
    path('liveproc/', views.liveproc, name='liveproc'),
    path('register/',views.register),
    path('sendotp/',views.sendEmailAndRegister),
    path('student/',views.studentDashboard),
    path('givetest/<int:id>',views.givetest),
    path('logout/',views.logout_view), 
    path('givesubtest/<int:id>',views.giveSubtest),
    path('payment/<int:id>',views.payment),
    path('instruction/<int:id>',views.instruction),
    path('video_feed/',views.videoFeed),
    path('student_log/',views.studentLogs),
    path('examlog/<int:id>',views.examlog),
    path('logdetails/<str:email>',views.logdetails),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)