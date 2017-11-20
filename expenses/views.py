from django import forms
from django.shortcuts import render, redirect

from expenses.forms import ExpenseForm
from expenses.models import Expense


def home(request):
    qs = Expense.objects.order_by('-date')
    d = {
        'objects': qs,
    }
    return render(request, "expenses/home.html", d)


def detail(request, id):
    o = Expense.objects.get(id=id)
    d = {
        'object': o,
    }
    return render(request, "expenses/detail.html", d)



def create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # assert False, form.cleaned_data
            # o = Expense()
            # o.title = request.POST['title']
            # o.amount = request.POST['amount']
            # o.date = request.POST['date']
            # o.description = request.POST['description']
            # o.save()
            o = form.save()
            return redirect("expenses:detail", id=o.id)
    else:
        # method = GET
        form = ExpenseForm()

    d = {
        'form': form,
    }
    return render(request, "expenses/form.html", d)
