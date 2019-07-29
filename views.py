from django.shortcuts import render
from hello_python.forms import User_reg
from hello_python.models import sign_up

def HelloBlog(request):
    return render(request,'user_blog.html')

def HelloContact(request):
    return render(request,'user_contact.html')

def Helloreg(request):

    obj=User_reg()

    if request.method=='POST':
        obj=User_reg(request.POST)
        if obj.is_valid():
            reg=sign_up()
            reg.username=obj.cleaned_data['username']
            reg.firstname=obj.cleaned_data['firstname']
            reg.lastname = obj.cleaned_data['lastname']
            reg.emailid = obj.cleaned_data['email_id']
            reg.address = obj.cleaned_data['address']
            reg.save()



    return render(request,'register.html',{ 'form':obj} )
