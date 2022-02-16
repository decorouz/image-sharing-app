
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from urllib import request
from urllib.request import Request, urlopen

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("title", "url", "description")
        widgets = {
            "url": forms.HiddenInput
        }

    def clean_url(self):
        """Verify provided image URL is valid"""
        url = self.cleaned_data["url"]

        valid_extensions = ["jpg", 'jpeg']
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                "The given URL does not match valid image extensions.")
        return url

    def save(self,
             force_insert=False,
             force_update=False,
             commit=True):
        image = super().save(commit=False)

        image_url = self.cleaned_data["url"]
        name = slugify(image.title)
        extension = image_url.rsplit(".", 1)[1].lower()
        image_name = f"{name}.{extension}"

        # download image from the given URL
        # response = request.urlopen(image_url)
        req = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        image.image.save(image_name,
                         ContentFile(urlopen(req).read()),
                         save=False)
        if commit:
            image.save()
        return image
