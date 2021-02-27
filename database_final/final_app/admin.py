from django.contrib import admin

# Register your models here.
from database_final.final_app.models import *
from django.contrib.auth.models import *

admin.site.register(Customers)
admin.site.register(EmployeePrivileges)
admin.site.register(Employees)
admin.site.register(InventoryTransactionTypes)
admin.site.register(InventoryTransactions)
admin.site.register(Invoices)
admin.site.register(OrderDetails)
admin.site.register(OrderDetailsStatus)
admin.site.register(Orders)
admin.site.register(OrdersStatus)
admin.site.register(OrdersTaxStatus)
admin.site.register(Privileges)
admin.site.register(Products)
admin.site.register(PurchaseOrderDetails)
admin.site.register(PurchaseOrderStatus)
admin.site.register(PurchaseOrders)
admin.site.register(SalesReports)
admin.site.register(Shippers)
admin.site.register(Strings)
admin.site.register(Suppliers)
