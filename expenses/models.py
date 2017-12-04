from django.db import models


# class Tag(models.Model):
#     name = models.CharField(max_length=100)


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    # tags = models.ManyToManyField(Tag, blank=True, related_name="expenses")

    def __str__(self):
        return self.title


class Comment(models.Model):
    expense = models.ForeignKey(Expense, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
