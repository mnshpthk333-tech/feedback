from .models import Profile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.
class CreateProfileView(CreateView):
    template_name = "profiles/profiles.html"
    model = Profile
    fields = '__all__'
    success_url = '/profiles/'

class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/all_profiles.html"
    context_object_name = "profiles"
