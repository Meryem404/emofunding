from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        print('SUBMITTED REG')
        redirect('accounts/register.html')
        #Get form values
       # first_name = request.POST['First Name']
       # last_name = request.POST['Last Name']
        #email = request.POST['Email Adress']
        #password = request.POST['Password']
        #password2 = request.POST['Repeat Password']

        #check if password match
        #if password == password2:

       # else:
    else:
        return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashbord(request):
    return render(request, 'accounts/dashbord.html')

