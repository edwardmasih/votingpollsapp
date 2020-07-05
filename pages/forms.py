from django import forms
from polls.models import Question, Choice

class AddQuestionForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Question

class AddChoices(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Choice