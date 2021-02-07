from django.db import models

# Create your models here.
class product(models.Model):
    # If no Primary Key is defined, it will create one for you automatically by the name of id and type int
    prod_id = models.IntegerField(primary_key=True,)
    name = models.CharField(max_length=50)

    date_of_exp= models.DateField()
    is_gold_prod = models.BooleanField()

# create a subclass to tell orm that the changes in databased are to be managed by it
    class Meta:
        managed = True
