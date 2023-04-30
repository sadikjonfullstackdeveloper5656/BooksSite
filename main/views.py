from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def main_page(request: HttpRequest):
    # result = 0
    # for i in range(100):
    #     result += i
    return HttpResponse(f"<h1> HELLO DJANGO </h1> <img src='https://img.freepik.com/free-photo/green-black-bugatti-veyron-with-black-yellow-paint_1340-23339.jpg?w=1060&t=st=1682861207~exp=1682861807~hmac=2d599f13eea3b0422978ae22c656564c81bd7b1da170dba6905bbccbc49bf4c9' alt='Rasm bor edi!' <br> <a href='/about/'>About</a> <a href='/contact/'>Contact</a> ")  #Result:{result}

def about_page(request: HttpRequest):
    print(request.method, request.content_type, request.user, request.path)

    return HttpResponse("<h1 style='text-align: center'> About page </h1> <a href='/'>Home</a> <a href='/contact/'>Contact</a>")

def contact_page(request: HttpRequest):
    return HttpResponse("<h1 >Contact Page </h1> <a href='/about/'>About</a> <a href='/'>Home</a> ")
    

# Create your views here.
