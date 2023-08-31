from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Text

# Create your views here.

def getComments():
    returnList = []
    for comment in Text.objects.all():
        returnList.append([comment.user_name, comment.input_text])
    returnList.reverse()
    return returnList

def index(request):
    if request.method == "POST":
        # code to save comment in db
        if request.POST.get("name") and request.POST.get("comment"):
            comment = Text(user_name=request.POST.get("name"), input_text=request.POST.get("comment"))
            comment.save()
            return redirect(request.path)
        
    returnList = getComments()
    context = {"comments": returnList}
    return render(request, "dbApp/index.html", context)
