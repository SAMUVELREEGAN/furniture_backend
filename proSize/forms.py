# app/forms.py
from django import forms
from .models import ProductSize

class ProductSizeForm(forms.ModelForm):
    size1 = forms.CharField(required=False)
    size2 = forms.CharField(required=False)
    size3 = forms.CharField(required=False)
    size4 = forms.CharField(required=False)
    size5 = forms.CharField(required=False)
    size6 = forms.CharField(required=False)
    size7 = forms.CharField(required=False)
    size8 = forms.CharField(required=False)
    size9 = forms.CharField(required=False)
    size10 = forms.CharField(required=False)
    size11 = forms.CharField(required=False)
    size12 = forms.CharField(required=False)
    size13 = forms.CharField(required=False)
    size14 = forms.CharField(required=False)
    size15 = forms.CharField(required=False)

    class Meta:
        model = ProductSize
        fields = ['category']  # We'll handle sizes manually

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If instance exists, pre-fill sizes
        if self.instance and self.instance.sizes:
            sizes = self.instance.sizes.split(',')
            for i in range(min(15, len(sizes))):
                self.fields[f'size{i+1}'].initial = sizes[i].strip()

    def clean(self):
        cleaned_data = super().clean()
        sizes = [
            cleaned_data.get('size1'),
            cleaned_data.get('size2'),
            cleaned_data.get('size3'),
            cleaned_data.get('size4'),
            cleaned_data.get('size5'),
            cleaned_data.get('size6'),
            cleaned_data.get('size7'),
            cleaned_data.get('size8'),
            cleaned_data.get('size9'),
            cleaned_data.get('size10'),
            cleaned_data.get('size11'),
            cleaned_data.get('size12'),
            cleaned_data.get('size13'),
            cleaned_data.get('size14'),
            cleaned_data.get('size15'),
        ]
        sizes = [s.strip() for s in sizes if s]
        cleaned_data['sizes'] = ','.join(sizes)
        return cleaned_data

    def save(self, commit=True):
        self.instance.sizes = self.cleaned_data['sizes']
        return super().save(commit)
