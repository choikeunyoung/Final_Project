from django import forms
from .models import *


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = (
            "art_category",
            "title",
            "art_size",
            "painted_year",
            "painted_way",
            "content",
            "image",
            "price",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = [
            "title",
            "offer_price",
            "art",
            "content",
        ]