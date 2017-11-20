from django import forms

from expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


class MyForm(forms.Form):
    title = forms.CharField(max_length=123)
    agree_tos = forms.BooleanField()

