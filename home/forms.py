from django import forms





class UploadFileBucketForm(forms.Form):
    browse=forms.ImageField()