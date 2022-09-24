import email
from turtle import home
from urllib.request import Request
from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blogApp.models import Post

# Create your views here.


def home(request):
    # return HttpResponse("This is my home")                          #  To show direct string in the webpage
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):    
    if request.method == 'POST':                                                         # Handling the post request of contact to the DB
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']                                               # Send the data server side to the client side
        # print(name, email, phone, content)
                
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:       # To check user fill the form of not            
            messages.error(request, 'Please fill the form correctly !')                  # To display the error message to the user
        else:            
            contact = Contact(name=name, email=email,                                    # Create the Contact object
                              phone=phone, content=content)            
            contact.save()                                                               # And save to the DB            
            messages.success(
                request, "Your message has been successfully sent")                      # To display the successfull message to the user    
    return render(request, 'home/contact.html')                                          # And this return the view page


def search(request):
    query = request.GET['query']                                                    # Handling the get request performed by the search                  
    allPosts = Post.objects.filter(title__icontains=query)                          # Search in the post DB through the title keyword
    params = {'allPosts': allPosts}                                                 # Send the data server side to the client side
    return render(request, "home/search.html", params)
