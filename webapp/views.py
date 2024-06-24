from django.shortcuts import render, redirect
from myapp.models import servicedb, gallerydb,registerdb,employeedb, workdb
from webapp.models import messagedb
# Create your views here.
def indexpage(request):
    ser = servicedb.objects.all()
    emp = employeedb.objects.all()
    return render(request, "webhome.html", {'ser':ser, 'emp':emp})
def servicepage(req):
    ser = servicedb.objects.all()
    return render(req, "viewservice.html", {'ser':ser})
def viewgallery(req):
    data = servicedb.objects.all()
    gal = gallerydb.objects.all()
    ser = servicedb.objects.all()
    return render(req, "gallery.html", {'data':data, 'gal':gal, 'ser':ser})

def galleryview(req, sername):
    ser = servicedb.objects.all()
    gal = gallerydb.objects.filter(Title=sername)
    return render(req, "viewgallery.html", {'gal': gal, 'ser':ser})
def contactpage(req):
    ser = servicedb.objects.all()
    return render(req, "contact.html", {'ser':ser})
def aboutpage(req):
    ser = servicedb.objects.all()
    return render(req, "aboutus.html", {'ser':ser})
def message(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        mob = req.POST.get('mobile')
        msg = req.POST.get('message')
        obj = messagedb(Name=na, Email=em, Mobile=mob, Message=msg)
        obj.save()
        return redirect(contactpage)
def userloginpage(request):
    return render(request, "userlogin.html")
def userlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if registerdb.objects.filter(Username=uname, Password=pwd).exists():
            request.session['Username']=uname
            request.session['Password']=pwd
            return redirect(indexpage)
        else:
            return redirect(userloginpage)
    return redirect(userloginpage)
def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(userloginpage)
def saveuser(req):
    if req.method == "POST":
        na = req.POST.get('username')
        em = req.POST.get('email')
        mob = req.POST.get('mobile')
        pas = req.POST.get('password')
        obj = registerdb(Username=na, Email=em, Mobile=mob, Password=pas)
        obj.save()
        return redirect(userloginpage)
def workdesc(req):
    return render(req, "workdescription.html")
def sendworkpage(req):
    ser = servicedb.objects.all()
    return render(req, "sendwork.html", {'ser':ser})

def sendworks(req):
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
        return redirect(sendworkpage)

