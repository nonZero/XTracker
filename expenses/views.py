from django.shortcuts import render
from django.http import HttpResponse


# random.sample => 6 x 1-42
# 30% chance "today you are lucky" / "not lucky"
# random color for each number

def home(request):
    d = {
        'foo': 'hello world',
        'bar': 100 * 42 * 2.5,
        'baz': [91, 45, 111],
    }
    return render(request, "expenses/home.html", d)
