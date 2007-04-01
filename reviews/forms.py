from django import forms
from voiture.models import Reviews



class ReviewsForm(forms.ModelForm):
    
    class Meta:
        model = Reviews
        exclude = ("created_at", "updated_at", "auteur", "voiture")
        widgets = {
            'reviews': forms.Textarea(
				attrs={
					'class': 'form-control',
					'placeholder': 'lorem ipsum',
				}
			),
        }