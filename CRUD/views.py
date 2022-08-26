from django.shortcuts import render,redirect
from CRUD.models import register
from django.contrib import messages

# Create your views here.

# Indexpage/Homepage
def index(request):
  return render(request,"registerform.html")

# Value Insert
def valueinsert(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    register(name = name, email = email, contact = contact).save()
    messages.success(request,"Value Inserted Successfully")
    return render(request,"registerform.html")
    # return redirect (viewlist)
  else:
    return render(request,"404.html")

# Value Listed
def viewlist(request):
  return render(request,"viewlist.html")
