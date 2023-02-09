from django.shortcuts import render, redirect
from .models import category, item
from django.contrib.auth import authenticate, login, logout
from .forms import registerForm
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm, AdminPasswordChangeForm

# Create your views here.
def index(request):
    items = item.objects.filter(is_sold = False)[0:6]
    categories = category.objects.all() 
    return render(request, 'core/index.html', 
    {
        'items': items,
        'categories': categories
    })
def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)

        if form.is_valid():
            user=form.save();
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('/login')
        messages.warning(request, 'Unsuccesful')
    form = registerForm()
    return render(request, 'core/register.html', {'form': form})

# def as_view(request):
    # if request.method == "POST":
    #     form = AuthenticationForm(request, data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             messages.info(request, f"You are now logged in as {username}.")
    #             return redirect("main:homepage")
    #         else:
    #             messages.error(request,"Invalid username or password.")
    #     else:
    #         messages.error(request,"Invalid username or password.")
    # form = AuthenticationForm()
    # return render(request, '')

def signout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('/')