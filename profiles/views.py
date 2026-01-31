from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import Profile
# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        Form = ProfileForm()
        return render(request, "profiles/profiles.html", {"form": Form})

    def post(self, request):
        Submitted_form=ProfileForm(request.POST, request.FILES)

        if Submitted_form.is_valid():
            profile=Profile(user_image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect("/profiles")
        else:
            return render(request, "profiles/profiles.html", {"form": Submitted_form}) 
    