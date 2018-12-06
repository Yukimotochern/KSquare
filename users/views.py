from django.shortcuts import render
from .forms import CustomUserCreationForm, ProfileForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.


# User Part

def register(request):

    registered = False

    if request.method == "POST":
        user_form = CustomUserCreationForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'registration/registration.html', locals())


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



