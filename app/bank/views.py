from bank.models import Branch, Account, Customer, Product
from rest_framework import viewsets
from bank.serializers import BranchSerializer, AccountSerializer, CustomerSerializer, ProductSerializer
from bank.models import Branch, Account, Customer, Product
from django.http import HttpResponse


class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

def branch_create(request):
    url_bank = request.GET.get('newbank')
    url_location = request.GET.get('newlocation')
    Branch.objects.create(
        bank=url_bank,
        location=url_location,
    )
    query_response = Branch.objects.all()
    return HttpResponse(query_response.values())

def branch_read(request):
    url_bank = request.GET.get('bank')
    query_response = Branch.objects.get(
        bank=url_bank
    )
    return HttpResponse(query_response)



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