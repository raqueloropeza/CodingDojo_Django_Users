from django.shortcuts import render, redirect
from .models import Users

#Main route that displays all records in user model.
def index(request):
    context = {
        "all_the_users": Users.objects.all()
    }
    return render(request, "index.html", context)

#Route /users creates input fields from POST method and redirects to index route. 
def create(request):
    new_user = Users.objects.create(first_name= request.POST["firstname"], last_name= request.POST["lastname"], email_address= request.POST["email"], age= request.POST["age"])
    return redirect ("/")


