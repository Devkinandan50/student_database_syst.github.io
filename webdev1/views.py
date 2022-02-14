from django.http import HttpResponse, response
from django.shortcuts import render
from myapp.models import Studentdata

def home(request):
    return render(request,'index.html')
def login(request):            #post is use for private data
    username=request.POST.get("unname") #if data is not private we also use GET
    password=request.POST.get("pass")
    if((username=="admin") and (password=="admin")):
        return render(request, 'studentdata.html')
    else:
        return HttpResponse("<h1>login fail</h1>")

def studentdata(request):
        name=request.POST.get("sname")
        college=request.POST.get("spass")
        roll=request.POST.get("numbe")
        branch=request.POST.get("branch")
    
        #mydict={'name':name, 'email':college, 'roll':roll, 'branch':branch}
        #return render(request, 'showdata.html', {'dict':mydict})

        vobj=Studentdata(studentname=name, studentcollege=college, studentrollnumber=roll, studentbranch=branch)  #call object of class which made in models.py
        vobj.save()
        print("Record save in Database")

        return render(request, 'saveornot.html')

#print data first row show in powershell or terminal of vs code 
'''def viewdata(request):
    studentobj=Studentdata.objects.all()
    print(studentobj)                     
    return render(request, 'index.html') '''

#print orginal data in powershell by using for loop 
'''def viewdata(request):
    studentobj=Studentdata.objects.all()
    for s in studentobj:
        print("student id",s.id)
        print("student name",s.studentname)
        print("student roll number",s.studentrollnumber)
        print("student branch",s.studentbranch)
        print("student college",s.studentcollege)
    return render(request, 'index.html') '''

#print orginal data in new html file
def viewdata(request):
    studentobj=Studentdata.objects.all()
    
    return render(request, 'view_all_data.html',{'data':studentobj})

def update_path(request): 
    #obj1=Studentdata.objects.all()
    return render(request,'edit.html')  

def update(request):
    upd=request.POST.get("s_id")

    name=request.POST.get("upname")
    college=request.POST.get("uppass")
    roll=request.POST.get("upnumbe")
    branch=request.POST.get("upbranch")

    vobj=Studentdata(id=upd, studentname=name, studentcollege=college, studentrollnumber=roll, studentbranch=branch) 
    vobj.save()
    print("Record save in Database")
    return render(request, 'saveornot.html')

def destroy_path(request):  
    return render(request, 'deletedata.html')

def destroy(request):
    deleted=request.POST.get("d_id")
    vobj=Studentdata(id=deleted)
    vobj.delete()
    return HttpResponse("<h1>Your data of this id is delete</h1>")

