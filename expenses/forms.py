from django import forms

from expenses.models import Expense, Comment


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )


class MyForm(forms.Form):
    title = forms.CharField(max_length=123)
    agree_tos = forms.BooleanField()

