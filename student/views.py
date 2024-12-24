from django.shortcuts import render

def setcookie(request):
    response = render(request,'student/setcookie.html')
    response.set_cookie('name','akshay')
    return response

def getcookie(request):
    name = request.COOKIES['name']
    return render(request,'student/getcookie.html',{'name':name})

def delcookie(request):
    response = render(request,'student/delcookie.html')
    response.delete_cookie('name')
    return response
    