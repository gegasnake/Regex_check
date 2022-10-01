from django import forms


class RegexCheckForm(forms.Form):
    text = forms.CharField(label="string to check",  max_length=200)
    pattern = forms.CharField(label="pattern to match", max_length=200)
