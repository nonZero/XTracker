import random

import silly
from django.core.management.base import BaseCommand
from django.db import transaction

from expenses.models import Expense


class Command(BaseCommand):
    help = "Create new expenses."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, **options):

        # Expense.objects.all().delete()

        for i in range(n):
            self.create_random_expense()

    def create_random_expense(self):
        with transaction.atomic():
            o = Expense()
            o.title = silly.a_thing()
            o.amount = "{}.{}".format(random.randint(1, 100),
                                      random.randint(0, 99))
            o.date = silly.datetime().date()
            o.description = "\n".join(
                [silly.paragraph(), silly.paragraph(), silly.paragraph()])
            o.save()

            for j in range(random.randint(0, 5)):
                text = "\n".join(
                    [silly.paragraph(), silly.paragraph(), silly.paragraph()])
                o.comments.create(content=text)

