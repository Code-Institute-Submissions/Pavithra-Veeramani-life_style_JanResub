from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 150,
        'rows': 3,
    }))

    class Meta:
        model = Review
        fields = ('content',)
