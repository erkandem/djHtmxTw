from django import forms

from .models import Party


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = (
            "party_date",
            "party_time",
            "venue",
            "invitation",
        )
        widgets = {
            "party_date": forms.DateInput(attrs={"type": "date"}),
            "party_time": forms.TimeInput(attrs={"type": "time"}),
            "invitation": forms.Textarea(attrs={"class": "w-full"}),
        }
