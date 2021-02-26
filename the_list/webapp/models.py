from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class List(models.Model):
    description = models.TextField(null=False, blank=False, verbose_name='Text')
    status = models.CharField(max_length=200, null=False, blank=False, choices=status_choices,
                              default=status_choices[0],
                              verbose_name='Status')
    created_at = models.DateField(null=True, blank=True, verbose_name='Change time')

    def __str__(self):
        return self.description
