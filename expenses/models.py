from django.db import models
from django.urls.base import reverse
from django.utils.translation import ugettext_lazy as _


class Expense(models.Model):
    date = models.DateField(_("date"))
    amount = models.DecimalField(_("amount"), max_digits=12, decimal_places=2)
    title = models.CharField(_("title"), max_length=300)
    description = models.TextField(_("description"), blank=True)

    class Meta:
        verbose_name = _("expense")
        verbose_name_plural = _("expenses")

    # tags = models.ManyToManyField(Tag, blank=True, related_name="expenses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.id,))

    def comments_by_date(self):
        return self.comments.order_by('-created_at')


class Comment(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.SET_NULL,
                                related_name="comments", null=True, blank=True,
                                verbose_name=_("expense"))
    created_at = models.DateTimeField(_("created at"),auto_now_add=True)
    content = models.TextField(_("content"))

    class Meta:  # holds some advanced setting for this model
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = (
            '-created_at',
        )
