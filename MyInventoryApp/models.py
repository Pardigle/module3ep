from django.db import models

class Supplier(models.Model):
    pass

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
