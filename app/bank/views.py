from bank.models import Branch, Account, Customer, Product
from rest_framework import viewsets
from bank.serializers import BranchSerializer, AccountSerializer, CustomerSerializer, ProductSerializer


class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer