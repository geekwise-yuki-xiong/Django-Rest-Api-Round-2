from django.db import models

class Branch(models.Model):
    class Meta:
        verbose_name_plural = 'branches'
    bank = models.CharField(max_length=300)
    location = models.CharField(max_length=300)

    def __str__(self):
        return(f"{self.bank}")

class Customer(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    def __str__(self):
        return(f"{self.pk}: {self.name} | {self.email}")

class Account(models.Model):
    bank_partner = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name='bank_partner',
    )
    holder = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
    )
    balance = models.DecimalField(max_digits=300, decimal_places=2)

    def __str__(self):
        return(f"Bank: {self.bank_partner.bank} | Account: {self.holder} | Balance: ${self.balance}")

class Product(models.Model):
    options = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
    )
    product_options = models.CharField(
        max_length=300,
        choices=options,
        default=options[0],
    )

    def __str__(self):
        return(f"{self.pk}: Product: {self.product_options}")