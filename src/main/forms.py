from django import forms
from .models import Question, Answer, Comment



class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ['title', 'content']



class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = ['title', 'content']

        

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
