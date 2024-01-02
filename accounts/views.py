from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from accounts.models import Person
from django.contrib.auth.decorators import login_required
from accounts.forms import PersonForm


# Create your views here.
def register_view(request):
    user_form = UserCreationForm(request.POST or None)
    if user_form.is_valid():
        user = user_form.save()
        person = Person.objects.create(user=user)
        return redirect('/accounts/login/')
    context={
        "user_form" : user_form,
    }
    return render(request, "accounts/register.html", context)


def login_view(request):
    if request.method == "POST":
        user_form = AuthenticationForm(request, data=request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            return redirect('/')
    else:
        user_form=AuthenticationForm(request)
    context={
        "user_form" : user_form,
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/accounts/login/')
    context = {

    }
    return render(request, "accounts/logout.html", context)


@login_required
def profile_view(request):
    if request.user.is_staff:
        person_object = None
    else:
        person_object = Person.objects.get(user=request.user)
    context = {
        'person_object' : person_object,
    }
    return render(request, "accounts/profile.html", context)


@login_required
def update_view(request):
    if request.user.is_staff:
        return redirect('/')
    person_object = get_object_or_404(Person, user=request.user)
    person_form = PersonForm(request.POST or None, instance=person_object)
    context = {
        "person_form" : person_form,
        "person_object" : person_object
    }
    if person_form.is_valid():
        person_form.save()
        context['message'] = 'Profile Updated'
        context['updated'] = True
        return redirect('/')
    return render(request, "accounts/update.html", context)


def change_password_view(request):
    if request.user.is_staff:
        return redirect('/')
    if request.method == 'POST':
        change_password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            logout(request)
            return redirect('/accounts/login/')
    else:
        change_password_form = PasswordChangeForm(user=request.user)
    context = {
        'change_password_form' : change_password_form
    }
    return render(request, 'accounts/change_password.html', context)