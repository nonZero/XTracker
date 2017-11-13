import random

import silly
from django.core.management.base import BaseCommand

from expenses.models import Expense


class Command(BaseCommand):
    help = "Create new expenses."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, **options):
        for i in range(n):
            o = Expense()
            o.title = silly.a_thing()
            o.amount = "{}.{}".format(random.randint(1, 100),
                                      random.randint(0, 99))
            o.date = silly.datetime().date()
            o.description = "\n".join(
                [silly.paragraph(), silly.paragraph(), silly.paragraph()])
            o.save()
