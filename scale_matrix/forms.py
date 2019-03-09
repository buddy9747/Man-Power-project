from django import forms
from .models import Scale

class ScaleForm(forms.ModelForm):

    class Meta:
        model = Scale
        fields = ('operation', 'level', 'skill_desc' )
'''
    def save(self, request, commit=True):
        model = super(ScaleForm, self).save(commit=False)

        model.usr = request.user.username

        if commit:
            model.save()

        return model'''


'''
import django_tables2 as tables

class SimpleTable(tables.Table):

    class Meta:
        model = Scale'''