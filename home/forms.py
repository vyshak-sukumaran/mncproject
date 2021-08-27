from django import forms

from .models import Review, Unknown

CHOICES = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)


class ReviewForm(forms.ModelForm):

    post = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 'rows': 5, 'cols': 100
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
