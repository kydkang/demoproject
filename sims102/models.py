from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from commons.models import Description
from django.shortcuts import get_object_or_404
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class Index102(models.Model):       
    SEQUENCE = '102'
    description = models.ForeignKey(Description, on_delete=models.CASCADE) 
    data_one = models.IntegerField(_('FT'), validators=[MinValueValidator(0)])
    data_two = models.IntegerField(_('PT'), validators=[MinValueValidator(0)])
    calculated_value = models.DecimalField(_('NF'), max_digits=7, decimal_places=2, blank=True, )
 
    class Meta:
        permissions = [
            ("index102_contributor", "index102_contributor"), 
            ("index102_validator",   "index102_validator"), 
        ]
        ordering = ['id'] 

    def calculate(self):         ##  also need to change  ajax_calculate() function 
        try:
          calc_value = (self.data_one) / self.data_two * 100000
        except:
            print("An exception occurred")
        return calc_value

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        # self.description = Description.objects.get(sequence=self.SEQUENCE)
        self.description = get_object_or_404(Description, sequence=self.SEQUENCE)
        super(Index102, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.data_one) + ",    " + str(self.data_two) 

    def clean(self):
        if self.data_one > self.data_two: 
            raise ValidationError(_('Entered numbers are not correct.  Try again.'))

    # def get_absolute_url(self):
    #     # or  return reverse('sims102:index_detail', args=[str(self.id)])
    #     return reverse('sims102:index_detail', kwargs={'pk': str(self.id)})



