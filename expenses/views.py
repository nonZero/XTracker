from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from expenses.forms import ExpenseForm, CommentForm
from expenses.models import Expense


def home(request):
    qs = Expense.objects.order_by('-date')
    d = {
        'objects': qs,
    }
    return render(request, "expenses/home.html", d)


def home_json(request):
    qs = Expense.objects.order_by('-date')
    data = {
        'expenses': [
            {
                'id': o.id,
                'title': o.title
            }
            for o in qs]
    }
    return JsonResponse(data)


def detail(request, id):
    o = get_object_or_404(Expense, id=id)

    if request.method == "POST":
        import time
        time.sleep(3)
        form = CommentForm(request.POST)
        form.instance.expense = o
        if form.is_valid():
            c = form.save()
            return render(request, "expenses/_comment.html", {
                'c': c,
            })
        return HttpResponseForbidden(
            form.errors.as_json(),
            content_type='application/json')

    d = {
        'object': o,
        'form': CommentForm(),
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


# def create_comment(request, id):
#     o = get_object_or_404(Expense, id=id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         form.instance.expense = o
#         if form.is_valid():
#             c = form.save()
#             return redirect(o)
#     else:
#         # method = GET
#         form = CommentForm()
#
#     d = {
#         'form': form,
#     }
#     return render(request, "expenses/comment_form.html", d)
