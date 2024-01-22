from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Product Name')
    code = models.CharField(max_length=50,blank=True, null=True,verbose_name='Product Code')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pro_product'

    def __str__(self):
        return str(self.name)