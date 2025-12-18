from django import forms
from .models import AirportRoute, Airport


class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ['parent_airport', 'child_airport', 'position', 'duration']

    def clean(self):
        cleaned_data = super().clean()

        parent = cleaned_data.get('parent_airport')
        child = cleaned_data.get('child_airport')
        duration = cleaned_data.get('duration')

        if parent and child and parent == child:
            raise forms.ValidationError(
                "Parent airport and child airport must be different."
            )

        if duration is not None and duration <= 0:
            raise forms.ValidationError(
                "Duration must be greater than zero."
            )

        return cleaned_data


# class NthNodeSearchForm(forms.Form):
#     """
#     Search Nth Left / Right Node
#     """
#     airport_code = forms.CharField(label="Airport Code", max_length=10)
#     direction = forms.ChoiceField(
#         choices=(('left', 'Left'), ('right', 'Right'))
#     )
#     n = forms.IntegerField(min_value=1)

class NthNodeSearchForm(forms.Form):
    airport_code = forms.CharField(max_length=10)
    direction = forms.ChoiceField(
        choices=(('left', 'Left'), ('right', 'Right'))
    )
    n = forms.IntegerField(min_value=1)

    def clean_airport_code(self):
        code = self.cleaned_data.get('airport_code')

        if not Airport.objects.filter(code=code).exists():
            raise forms.ValidationError(
                "Airport with this code does not exist."
            )

        return code

# class ShortestPathForm(forms.Form):
#     """
#     Shortest path between two airports
#     """
#     source = forms.CharField(max_length=10)
#     destination = forms.CharField(max_length=10)


class ShortestPathForm(forms.Form):
    source = forms.CharField(max_length=10)
    destination = forms.CharField(max_length=10)

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('source')
        destination = cleaned_data.get('destination')

        if source == destination:
            raise forms.ValidationError(
                "Source and destination airports must be different."
            )

        if source and not Airport.objects.filter(code=source).exists():
            raise forms.ValidationError(
                "Source airport does not exist."
            )

        if destination and not Airport.objects.filter(code=destination).exists():
            raise forms.ValidationError(
                "Destination airport does not exist."
            )

        return cleaned_data


# class AirportForm(forms.ModelForm):
#     """
#     Form to create Airport
#     """
#     class Meta:
#         model = Airport
#         fields = ['code']

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code']

    def clean_code(self):
        code = self.cleaned_data.get('code')

        if not code:
            raise forms.ValidationError("Airport code is required.")

        if len(code) < 2:
            raise forms.ValidationError(
                "Airport code must be at least 2 characters long."
            )

        return code.upper()
