from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Text

# Create your views here.

def getComments():
    returnDict = {}
    for comment in Text.objects.all():
        returnDict[comment.user_name] = comment.input_text
    returnDict = dict(reversed(returnDict.items()))
    print(returnDict)
    return returnDict

def index(request):
    if request.method == "POST":
        # code to save comment in db
        if request.POST.get("name") and request.POST.get("comment"):
            comment = Text(user_name=request.POST.get("name"), input_text=request.POST.get("comment"))
            comment.save()
            return redirect(request.path)
        
    returnDict = getComments()
    print(returnDict)
    context = {"comments": returnDict}
    return render(request, "dbApp/index.html", context)
