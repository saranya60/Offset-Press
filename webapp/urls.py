from django.urls import path
from webapp import views
urlpatterns = [
    path('', views.indexpage, name="indexpage"),
    path('servicepage/', views.servicepage, name="servicepage"),
    path('viewgallery/', views.viewgallery, name="viewgallery"),
    path('galleryview/<sername>/', views.galleryview, name="galleryview"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('message/', views.message, name="message"),
    path('userloginpage/', views.userloginpage, name="userloginpage"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('workdesc/', views.workdesc, name="workdesc"),
    path('sendworkpage/', views.sendworkpage, name="sendworkpage"),
    path('sendworks/', views.sendworks, name="sendworks"),

]