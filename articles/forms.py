from typing import Any
from django import forms
from .models import Article


class ArtileForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =["title", "content"]

    def clean(self) -> dict[str, Any]:
        return super().clean()