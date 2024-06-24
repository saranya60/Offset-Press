from django.shortcuts import render, redirect
from myapp.models import servicedb, employeedb, gallerydb, workdb
from webapp.models import messagedb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

# Create your views here.
def loginpage(request):
    return render(request, "adminlogin.html")
def adminhome(request):
    return render(request, "AdminHome.html")
def admin_login(request):
    if request.method == "POST":
         uname = request.POST.get('username')
         pwd = request.POST.get('password')
         if User.objects.filter(username__contains=uname).exists():
             user = authenticate(username=uname, password=pwd)
             if user is not None:
                 login(request, user)
                 request.session['username'] = uname
                 request.session['password'] = pwd
                 return redirect(adminhome)
             else:
                 return redirect(loginpage)
         else:
             return redirect(loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def service(req):
    return render(req, "addservice.html")
def saveservice(req):
    if req.method == "POST":
        sr = req.POST.get('service')
        im = req.FILES['simage']
        obj = servicedb(Service=sr, Image=im)
        obj.save()
        return redirect(service)
def dispservices(req):
    data = servicedb.objects.all()
    return render(req, "displayservice.html", {'data':data})
def editservices(req, dataid):
    data = servicedb.objects.get(id=dataid)
    return render(req, "editservice.html", {'data':data})
def updateservice(req, dataid):
    if req.method == "POST":
        ser = req.POST.get('service')
        try:
            im = req.FILES['simage']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = servicedb.objects.get(id=dataid).Image
        servicedb.objects.filter(id=dataid).update(Service=ser, Image=file)
        return redirect(dispservices)
def deleteservice(req, dataid):
    data = servicedb.objects.filter(id=dataid)
    data.delete()
    return redirect(dispservices)

def emppage(req):
    return render(req, "addemployee.html")
def saveemployee(req):
    if req.method == "POST":
        na = req.POST.get('empname')
        mob = req.POST.get('mobile')
        em = req.POST.get('email')
        sal = req.POST.get('salary')
        im = req.FILES['simage']
        obj = employeedb(Empname=na, Mobile=mob, Email=em, Salary=sal, Image=im)
        obj.save()
        return redirect(emppage)
def dispemployee(req):
    data = employeedb.objects.all()
    return render(req, "employeedata.html", {'data': data})
def edit_emp(req, dataid):
        data = employeedb.objects.get(id=dataid)
        return render(req, "editemployee.html", {'data': data})
def update_emp(req, dataid):
    if req.method == "POST":
        na = req.POST.get('empname')
        mob = req.POST.get('mobile')
        em = req.POST.get('email')
        sal = req.POST.get('salary')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = employeedb.objects.get(id=dataid).Image
        employeedb.objects.filter(id=dataid).update(Empname=na, Mobile=mob, Email=em, Salary=sal, Image=file)
        return redirect(dispemployee)
def delete_emp(req, dataid):
    data = employeedb.objects.filter(id=dataid)
    data.delete()
    return redirect(dispemployee)
def viewdata(req):
    return render(req, "viewtables.html")
def gallery(req):
    ser = servicedb.objects.all()
    return render(req, "imageupload.html", {'ser': ser})
def saveimage(req):
    if req.method == "POST":
        sr = req.POST.get('title')
        im = req.FILES['image']
        obj = gallerydb(Title=sr, Image=im)
        obj.save()
        return redirect(gallery)
def dispgallery(req):
    data = servicedb.objects.all()
    return render(req, "worksgallery.html", {'data':data})

def gallerypage(req, sername):
    gal = gallerydb.objects.filter(Title=sername)
    return render(req, "filteredgallery.html", {'gal': gal})
def viewmessage(req):
    msg = messagedb.objects.all()
    return render(req, "messageview.html", {'msg': msg})
def deleteimage(req, dataid):
    data = gallerydb.objects.filter(id=dataid)
    data.delete()
    return redirect(dispgallery)

def viewwork(request):
    work = workdb.objects.all()
    return render(request, "viewworks.html", {'work':work})

def addwork(request):
    ser = servicedb.objects.all()
    return render(request, "addworks.html", {'ser':ser})

def savework(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        mob = req.POST.get('mobile')
        con = req.POST.get('content')
        ser = req.POST.get('service')
        qt = req.POST.get('quantity')
        im = req.FILES['image']

        obj = workdb(Customer=na, Email=em, Mobile=mob, Content=con, ContentImage=im, Service=ser, quantity=qt)
        obj.save()
        return redirect(addwork)

def viewbill(req, dataid):
    
    if req.method == "POST":
        am = req.POST.get('amt')
        data = workdb.objects.get(id=dataid)
                                            
        return render(req, "bill.html", {'am':am, 'data':data})

def savebill(req):
    
    if req.method == "POST":
        am = req.POST.get('amt')
        
        workdb.objects.filter(id=dataid).update(Amount=am)                                 
        return redirect(viewwork)

