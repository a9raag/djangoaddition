from django.db import models


class Numbers(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()

    def __unicode__(self):
        return self.number1 + self.number2
