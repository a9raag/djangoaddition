from django import forms
import models


class Numbers(forms.Form):
    class Meta:
        model = models.Numbers
        fields = ['number1', 'number2']

    number1 = forms.IntegerField()
    number2 = forms.IntegerField()

