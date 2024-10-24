from django.shortcuts import render
from app1.models import Notes

# Create your views here.
def fun1(request):
    result=Notes.objects.all()
    if request.method=="POST":
        heading=request.POST.get("title")
        day=request.POST.get("date")
        about=request.POST.get("desc")

        obj=Notes(Title=heading,Date=day,Description=about)
        obj.save()
        result=Notes.objects.all()
        return render(request,"Insert.html",{"res":result , "obj":obj})
    return render(request,"Insert.html")



def fun2(request):
    result=Notes.objects.all()
    if request.method=="POST":
        Item=str(request.POST.get("title"))
        if Notes.objects.filter(Title=Item).exists():
            abc=Notes.objects.get(Title=Item) 
        else:
            abc=None
        return render(request,"record.html",{"res":result,"res2":abc})
    return render(request,"record.html")


def fun3(request):
    
    if request.method=="POST":

        heading=request.POST.get("title")
        if Notes.objects.filter(Title=heading):
            result=Notes.objects.all()
            abc=Notes.objects.get(Title=heading) 
            abc.delete()
        

   
            return render(request,"delete.html",{"result":result,"abc":abc})
    result=Notes.objects.all()
    return render(request,"delete.html", {"result":result})





