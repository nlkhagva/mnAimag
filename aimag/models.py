from django.db import models
# Create your models here.
class Aimag(models.Model):
    name        = models.CharField(max_length=30)
    sum_count   = models.IntegerField(default=0)
    hun_am      = models.IntegerField(default=0)
    talbai      = models.IntegerField(default=0)
    nyagtarshil = models.FloatField(default=0)
    aimag_tuv   = models.CharField(max_length=50)
    hursh_aimag = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name    

class Sum(models.Model):
    name        = models.CharField(max_length=50)
    aimag       = models.ForeignKey(Aimag, on_delete=models.CASCADE)
    bag_count   = models.IntegerField(default=0)
    hun_am      = models.IntegerField(default=0)
    talbai      = models.IntegerField(default=0)
    nyagtarshil = models.FloatField(default=0)
    hursh_sum   = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

