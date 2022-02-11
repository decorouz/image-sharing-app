
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from bookmarks import settings

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .tokens import account_activation_token

from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": dashboard})


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            email = request.POST.get("email")
            new_user = user_form.save(commit=False)
            new_user.is_active = False
            new_user.save()

            current_site = get_current_site(request)

            subject = "Activate your Account"
            message = render_to_string("account/account_activation_email.html", {
                "user": new_user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                "token": account_activation_token.make_token(new_user)

            })

            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False)
                messages.add_message(request, messages.SUCCESS,
                                     'A verification email has been sent.')
                messages.add_message(request, messages.WARNING,
                                     'Please also check your SPAM inbox!')
                return render(request,
                              'account/account_activation_sent.html',
                              {'new_user': new_user})
            except Exception as e:
                print(e)  # e.message
                messages.add_message(request, messages.WARNING, str(e))

    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})

# create user profile


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend)
        return redirect('dashboard')
    else:
        return render(request, 'account/account_activation_invalid.html')


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("dashboard")

        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
