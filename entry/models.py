from django.db import models

# Create your models here.
class Beer(models.Model):
    
    def __str__(self):
        return self.name.replace("_", " ")
        
    name = models.CharField(max_length = 100)
    purchDate = models.DateTimeField('Date Purchased')
    price = models.FloatField(default = 0.0)
    numSold = models.IntegerField('Number Sold', default = 0)
    lastPrice = models.FloatField(default = 0.0)
    priceChange = models.FloatField(default = 0.0)
    icon = models.IntegerField(default = 1)
    ABV = models.FloatField(default = 4.2)
    
class Sale(models.Model):
    
    def __str__(self):
        return str(self.beerSold) + ' ' + str(self.time)
        
    beerSold = models.ForeignKey(Beer, on_delete=models.CASCADE)
    time = models.DateTimeField('Time of Sale')
    quantity = models.IntegerField(default = 1)
    price = models.FloatField(default = 0.0)