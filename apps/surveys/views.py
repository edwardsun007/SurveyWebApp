from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages   # for display flash message on page

# Create your views here.
def index(request):
    if "surveys" not in request.session:
        request.session["surveys"]= []  # session is dictionary, surveys is array
    return render(request, "surveys/index.html")

# get inputs
def process(request):
    if request.method=="POST":
      print('request is POST method')
      # store user inputs in a new dictionary
      new_survey = {
          "full_name":request.POST.get("full_name"),
          "location":request.POST.get("location"),
          "language":request.POST.get("language"),
          "comment":request.POST.get("comment")
      }
      # Do some validation
      valid = True
      if new_survey["full_name"]=="":
          messages.error(request,"Name cannot be empty !")
          valid = False
      if new_survey["location"]=="":
          messages.error(request,"Location cannot be empty !")
          valid = False
      if new_survey["language"]=="":
          messages.error(request,"Language cannot be empty !")
      
      # if validation okay
      if valid == True:
          # get it fromm 
          surveys = request.session["surveys"]
          surveys.append(new_survey)
          request.session["surveys"]=surveys
          request.session.modified = True
          messages.success(request,"New survey got saved !")
    
      return redirect('/result')

def result(request):
    try:
        request.session['time']+=1
    except KeyError:
        request.session['time']=1
    # get surveys 
    surveys = request.session["surveys"]
    print('surveys: ',surveys)            # debug
    # the last submitted survey is indexed at -1
    last_survey = surveys[-1]   
    print('last_survey: ',last_survey)     # debug
    # we only need to fill the page with fields from the last survey remeber
    context = {
        "last_survey":last_survey
    }
    return render(request,"surveys/result.html",context)


def goBack(request):
    return redirect('/')