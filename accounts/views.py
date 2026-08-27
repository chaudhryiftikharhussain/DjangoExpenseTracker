from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    print(f"login view is called.... {request.method}")


    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            print("USer found")
            print(user)
            login(request, user)
            return redirect('/')
        else:
            print("User not found")

    form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'login.html', context=context)
