from django import forms
from .models import Recipe, KeyValueStore


# Custom recipe forms
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'image']


class RecipeSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        label='Search Recipes',
        widget=forms.TextInput(attrs={'placeholder': 'By name or ingredients...'})
    )


# Sample recipe forms
class KeyValueStoreForm(forms.ModelForm):
    class Meta:
        model = KeyValueStore
        fields = ['idmeal', 'stringredient1', 'strinstructions', 'image']


class KeyValueStoreSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        label='Search Recipes',
        widget=forms.TextInput(attrs={'placeholder': 'By name or ingredients...'})
    )