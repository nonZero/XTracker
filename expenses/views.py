from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from expenses.forms import ExpenseForm, CommentForm
from expenses.models import Expense


def home(request):
    qs = Expense.objects.order_by('-date')
    d = {
        'objects': qs,
    }
    return render(request, "expenses/home.html", d)


def detail(request, id):
    o = get_object_or_404(Expense, id=id)
    # try:
    #     o = Expense.objects.get(id=id)
    # except Expense.DoesNotExist:
    #     raise Http404("go away!")
    d = {
        'object': o,
    }
    return render(request, "expenses/detail.html", d)


def create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect("expenses:detail", id=o.id)
    else:
        # method = GET
        form = ExpenseForm()

    d = {
        'form': form,
    }
    return render(request, "expenses/form.html", d)


def create_comment(request, id):
    o = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        form.instance.expense = o
        if form.is_valid():
            c = form.save()
            return redirect(o)
    else:
        # method = GET
        form = CommentForm()

    d = {
        'form': form,
    }
    return render(request, "expenses/comment_form.html", d)


