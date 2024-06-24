from django.urls import path
from myapp import views
urlpatterns = [
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('service/', views.service, name="service"),
    path('saveservice/', views.saveservice, name="saveservice"),
    path('emppage/', views.emppage, name="emppage"),
    path('viewdata/', views.viewdata, name="viewdata"),
    path('dispservices/', views.dispservices, name="dispservices"),
    path('editservices/<int:dataid>/', views.editservices, name="editservices"),
    path('updateservice/<int:dataid>/', views.updateservice, name="updateservice"),
    path('deleteservice/<int:dataid>/', views.deleteservice, name="deleteservice"),
    path('saveemployee/', views.saveemployee, name="saveemployee"),
    path('dispemployee/', views.dispemployee, name="dispemployee"),
    path('edit_emp/<int:dataid>/', views.edit_emp, name="edit_emp"),
    path('update_emp/<int:dataid>/', views.update_emp, name="update_emp"),
    path('delete_emp/<int:dataid>/', views.delete_emp, name="delete_emp"),
    path('gallery/', views.gallery, name="gallery"),
    path('saveimage/', views.saveimage, name="saveimage"),
    path('dispgallery/', views.dispgallery, name="dispgallery"),
    path('gallerypage/<sername>/', views.gallerypage, name="gallerypage"),
    path('viewmessage/', views.viewmessage, name="viewmessage"),
    path('deleteimage/<int:dataid>/', views.deleteimage, name="deleteimage"),
    path('viewwork/', views.viewwork, name="viewwork"),
    path('addwork/', views.addwork, name="addwork"),
    path('savework/', views.savework, name="savework"),
    path('viewbill/<int:dataid>/', views.viewbill, name="viewbill"),
    path('savebill/', views.savebill, name="savebill")


]
