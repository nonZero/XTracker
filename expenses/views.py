import random
from django.shortcuts import render
from django.http import HttpResponse

# random.sample => 6 x 1-42
# 30% chance "today you are lucky" / "not lucky"
# random color for each number

COLORS = ['red', 'green', 'yellow', 'blue', 'orange', 'purple', 'cyan',
          'magenta', 'lime', 'pink', 'teal', 'lavender', 'brown', 'beige',
          'maroon', 'mint', 'olive', 'coral', 'navy', 'grey', 'white', 'black']


def home(request):
    n = 6
    lotto = sorted(random.sample(range(1, 43), n))
    # color = random.choice(COLORS)
    colors = random.sample(COLORS, n)

    pairs = zip(lotto, colors)

    d = {
        # 'values': lotto,
        # 'color': color,
        'values': pairs,
    }
    return render(request, "expenses/home.html", d)
