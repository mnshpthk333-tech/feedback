from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm

# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        Form = ProfileForm()
        return render(request, "profiles/profiles.html", {"form": Form})

    def post(self, request):
        Submitted_form=ProfileForm(request.POST, request.FILES)

        if Submitted_form.is_valid():
            store_file(request.FILES["image"])
            return HttpResponseRedirect("/profiles")
        else:
            return render(request, "profiles/profiles.html", {"form": Submitted_form}) 
    