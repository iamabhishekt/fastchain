# view.py is controller in MVC model 
# It handles all business logic, getting a processing data
# in here and pass it to the front end which is view
from django.shortcuts import render

# Create your views here.

# home function is a controller to render home.html 
def home(request): # from urls.py connects views.py --> home function is an action
    return render(request, 'home.html') # request --> frontend templates/home.html which act as a view inside MVC model 

# customer_page function is a controller to render home.html
def customer_page(request): # from urls.py connects views.py --> customer_page function is an action
    return render(request, 'home.html') # request --> frontend templates/home.html which act as a view inside MVC model 

# courier_page function is a controller to render home.html
def courier_page(request): # from urls.py connects views.py --> courier_page function is an action
    return render(request, 'home.html') # request --> frontend templates/home.html which act as a view inside MVC model 



     