from django.shortcuts import render, redirect


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def contact(request):
    return render(request, 'contact.html')


def employerhomepage(request):
    if request.user.is_authenticated and len(request.user.username) == 4:
        return render(request, 'employerhomepage.html')
    else:
        return redirect('login')


def jobseekerhomepage(request):
    if request.user.is_authenticated and len(request.user.username) == 10:
        return render(request, 'jobseekerhomepage.html')
    else:
        return redirect('login')


def about(request):
    return render(request, 'about.html')


def company(request):
    return render(request, 'company.html')


def service(request):
    return render(request, 'service.html')


def signup(request):
    return render(request, 'signup.html')


from django.contrib import messages
from django.contrib.auth.models import User, auth


def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username Already Taken.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, 'Account created successfully')
                user_details = {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name
                }
                return render(request, 'homepage.html',
                              {'user_details': user_details})  # Redirect to account details page
        else:
            messages.info(request, 'Password does not match')
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('jobseekerhomepage')
            elif len(username) == 4:
                return redirect('employerhomepage')
            else:
                return redirect('homepage')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'homepage.html')


def read(request):
    return render(request, 'read.html')


def forgot_password(request):
    return render(request, 'forgot_password.html')


def account_details(request):
    user_details = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
    }
    user_role = 'Employer' if len(request.user.username) == 4 else 'Job Seeker'
    return render(request, 'account_details.html', {'user_details': user_details, 'user_role': user_role})


def user_profile(request):
    return render(request, 'user_profile.html')