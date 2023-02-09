from django import forms
from core.models import item

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ("category", "name", "description", "image", "price", "slashed")
        
        widgets = {
            'category': forms.Select(attrs={
                'class': 'input-form'
            }),
            'name': forms.TextInput(attrs={
                'class': 'input-form'
            }),
            'description': forms.Textarea(attrs={
                'class': 'input-form'
            }),
            'price': forms.TextInput(attrs={
                'class': 'input-form'
            }),
            'image': forms.FileInput(attrs={
                'class': 'input-form'
            })
        }