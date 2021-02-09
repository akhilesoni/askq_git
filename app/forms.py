from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class AskQuestion(forms.Form):
    question = forms.CharField(max_length=200)
    topic = forms.CharField(max_length=50)  

class AddTopicForm(forms.Form):
    topic = forms.CharField(max_length=50)


class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=200)