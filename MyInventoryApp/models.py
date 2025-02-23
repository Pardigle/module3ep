from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def getName(self):
        return self.name
   
    def __str__(self):
        return "{} - {}, {} created at: {}".format(self.name, self.city, self.country, self.created_at)

class WaterBottle(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    mouthSize = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    suppliers = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    currentQuantity = models.IntegerField()

    def __str__(self):
        return f"SKU: {self.sku}, {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplier.name}, Cost: {self.cost}, Quantity: {self.current_quantity}"
