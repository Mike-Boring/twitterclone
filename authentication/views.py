from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
from authentication.forms import LoginForm, SignupForm
from twitteruser.models import TwitterUser

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homeview")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homeview"))


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get("username").lower(), password=data.get("password"), first_name=data.get("firstname"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homeview"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})
