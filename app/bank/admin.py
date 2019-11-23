from django.contrib import admin
from bank.models import Branch, Account, Customer, Product

# Register your models here.
admin.site.register((
    Account,
    Customer,
    Product,
))

class BranchInline(admin.StackedInline):
    model = Branch

class AccountInline(admin.StackedInline):
    model = Account

class CustomerInline(admin.StackedInline):
    model = Customer

class ProductInline(admin.StackedInline):
    model = Product

@admin.register(Branch)
class AccountAdmin(admin.ModelAdmin):
    inlines = [
        AccountInline,
    ]

# @admin.register()
# class AccountAdmin(admin.ModelAdmin):
#     inlines = [
#         AccountInline,
#     ]

