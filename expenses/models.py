from django.db import models
from django.urls.base import reverse


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    # tags = models.ManyToManyField(Tag, blank=True, related_name="expenses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.id,))

    def comments_by_date(self):
        return self.comments.order_by('-created_at')


class Comment(models.Model):
    expense = models.ForeignKey(Expense, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:  # holds some advanced setting for this model
        ordering = (
            '-created_at',
        )
