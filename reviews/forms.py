from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        labels={
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating"
        }
        error_messages = {
            "user_name":{
                "required":"Your name not must be empty!",
                "max_length":"Please enter shorter text!"
            }
        }