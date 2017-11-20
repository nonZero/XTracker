from django.shortcuts import render

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
