from django import forms
from django.forms import ModelForm



from .models import LeaveApplication



class LeaveApplicationForm(ModelForm):

    class Meta:
        model = LeaveApplication
        fields = ('leave_id','start_date', 'end_date', 'leave_category','leave_reason' )
    '''
    def save(self, request, commit=True):
        model = super(LeaveApplicationForm, self).save(commit=False)

        model.usr = request.user.username

        if commit:
            model.save()

        return model
    '''
    def clean_end_date(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date >= start_date:
            return end_date
        else:
            raise forms.ValidationError("'End Date' should be "
                                        "after 'Start Date' .")
