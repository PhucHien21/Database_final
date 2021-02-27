from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from database_final.final_app.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from .models import *
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    
    
class EmployeePrivilegeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EmployeePrivileges to be viewed or edited.
    """
    queryset = EmployeePrivileges.objects.all()
    serializer_class = EmployeePrivilegesSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Employees to be viewed or edited.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class InventoryTransactionTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows InventoryTransactionTypes to be viewed or edited.
    """
    queryset = InventoryTransactionTypes.objects.all()
    serializer_class = InventoryTransactionTypesSerializer


class InventoryTransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows InventoryTransactions to be viewed or edited.
    """
    queryset = InventoryTransactions.objects.all()
    serializer_class = InventoryTransactionsSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Invoices to be viewed or edited.
    """
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderDetails to be viewed or edited.
    """
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer


class OrderDetailStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderDetailsStatus to be viewed or edited.
    """
    queryset = OrderDetailsStatus.objects.all()
    serializer_class = OrderDetailsStatusSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrdersStatus to be viewed or edited.
    """
    queryset = OrdersStatus.objects.all()
    serializer_class = OrdersStatusSerializer


class OrderTaxStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrdersTaxStatus to be viewed or edited.
    """
    queryset = OrdersTaxStatus.objects.all()
    serializer_class = OrdersTaxStatusSerializer


class PrivilegeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Privileges to be viewed or edited.
    """
    queryset = Privileges.objects.all()
    serializer_class = PrivilegesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class PurchaseOrderDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PurchaseOrderDetails to be viewed or edited.
    """
    queryset = PurchaseOrderDetails.objects.all()
    serializer_class = PurchaseOrderDetailsSerializer


class PurchaseOrderStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PurchaseOrderStatus to be viewed or edited.
    """
    queryset = PurchaseOrderStatus.objects.all()
    serializer_class = PurchaseOrderStatusSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PurchaseOrders to be viewed or edited.
    """
    queryset = PurchaseOrders.objects.all()
    serializer_class = PurchaseOrdersSerializer


class SaleReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SalesReports to be viewed or edited.
    """
    queryset = SalesReports.objects.all()
    serializer_class = SalesReportsSerializer


class ShipperViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Shippers to be viewed or edited.
    """
    queryset = Shippers.objects.all()
    serializer_class = ShippersSerializer

class StringViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Strings to be viewed or edited.
    """
    queryset = Strings.objects.all()
    serializer_class = StringsSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Suppliers to be viewed or edited.
    """
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer