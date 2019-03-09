from django import forms
from .models import *

class ProductionForm(forms.ModelForm):
    class Meta:
        model=Production
        fields=['serial_no','hourly_achieved','hourly_running_ticket_no']
class QualityForm(forms.ModelForm):
    class Meta:
        model=Quality
        fields=['rework_ticket_no','repair_ticket_no','finish_return_ticket_no',
                'cutting_defects_ticket_no','cutting_missing_ticket_no',
                    'holding_ticket_no']

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model=Maintenance
        fields=['waiting','setting','breakdown','power_failure']

class PlanChangeForm(forms.ModelForm):
    class Meta:
        model=PlanChange
        fields=['machine_issue','quality_issue','trims_issue','others',
                'delay_start','demo','learning','full_swing']

class Dashselect(forms.ModelForm):
    class Meta:
        model = Production
        fields = ('user',)

