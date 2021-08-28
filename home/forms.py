from django import forms

from .models import Review, Unknown, CHOICES



class ReviewForm(forms.ModelForm):

    post = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 'rows': 5, 'cols': 100
            }
        )
    )
    rating = forms.IntegerField(
        widget=forms.Select(
            choices=CHOICES,
            attrs={
                'class':'form-control'
            }
            )
        )

    class Meta:
        model = Review
        fields = ['post', 'rating']

class UnknownForm(forms.ModelForm):

    post = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 'rows': 5, 'cols': 100,
                "id": "message-text"
            }
        )
    )
    class Meta:
        model = Unknown
        fields = ['post']
