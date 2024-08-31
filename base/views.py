from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if remember_me:
                request.session.set_expiry(604800)
            else:  
                request.session.set_expiry(0)   
            
            login(request, user)  #updated code to save login data into the session
            request.session['username'] = username  # Store username in session
            messages.success(request, 'Login successful.')
            # Print to nderstand whats happening
            print("User authenticated:", user)
            print("Session username after login:", request.session.get('username'))
            
            return redirect('accounts/profile/') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'base/login.html')