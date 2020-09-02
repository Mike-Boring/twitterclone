from django import forms


class TweetForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
