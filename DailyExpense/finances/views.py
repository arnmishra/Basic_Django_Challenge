from django.shortcuts import render
from finances.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'finances/index.html', context_dict)

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'finances/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/finances/')
            else:
                return HttpResponse("Your Finances account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'finances/login.html', {})

@login_required
def user_logout(request):
	
    logout(request)
    return HttpResponseRedirect('/finances/')

def submit_expense(request):

    if request.method == 'POST':
    	return HttpResponse("Success! <br/> <a href='/finances/'>Return to Home</a>")

    return render(request, 'finances/submit_expense.html', {})
