from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

from allauth.account.internal.flows.email_verification import (
    send_verification_email_to_address,
)
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from .forms import *


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            # return redirect('account_login')
            return redirect_to_login(request.get_full_path())
    return render(request, "a_users/profile.html", {"profile": profile})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")

    if request.path == reverse("profile-onboarding"):
        onboarding = True
    else:
        onboarding = False

    context = {
        "form": form,
        "onboarding": onboarding,
    }
    return render(request, "a_users/profile_edit.html", context)


@login_required
def profile_settings_view(request):
    return render(request, "a_users/profile_settings.html")


@login_required
def profile_emailchange(request):

    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, "_partials/_email_form.html", {"form": form})

    if request.method == "POST":
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():

            # Check if the email already exists
            email = form.cleaned_data["email"]
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f"{email} est déjà utilisé.")
                return redirect("profile-settings")

            form.save()

            # Then Signal updates emailaddress and set verified to False

            # Then send confirmation email
            # send_email_confirmation() will be deprecated soon!
            email_address = EmailAddress.objects.get_primary(request.user)
            send_verification_email_to_address(request, email_address)
            # send_email_confirmation(request, request.user)

            return redirect("profile-settings")
        else:
            messages.warning(request, "Email invalide ou déjà utilisé")
            return redirect("profile-settings")

    return redirect("profile-settings")


@login_required
def profile_usernamechange(request):
    if request.htmx:
        form = UsernameForm(instance=request.user)
        return render(request, "_partials/_username_form.html", {"form": form})

    if request.method == "POST":
        form = UsernameForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Nom d'utilisateur mis à jour.")
            return redirect("profile-settings")
        else:
            messages.warning(request, "Nom d'utilisateur invalide ou deja utilisé.")
            return redirect("profile-settings")

    return redirect("profile-settings")


@login_required
def profile_emailverify(request):
    # send_email_confirmation(request, request.user)
    email_address = EmailAddress.objects.get_primary(request.user)
    send_verification_email_to_address(request, email_address)
    return redirect("profile-settings")


@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, "Compte supprimé, quel dommage !")
        return redirect("home")
    return render(request, "a_users/profile_delete.html")
