from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from database_final.final_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'employeeprivilege', views.EmployeePrivilegeViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'inventorytransationtype',
                views.InventoryTransactionTypeViewSet)
router.register(r'inventorytransaction', views.InventoryTransactionViewSet)
router.register(r'invoice', views.InvoiceViewSet)
router.register(r'orderdetail', views.OrderDetailViewSet)
router.register(r'orderdetailstatus', views.OrderDetailStatusViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderstatus', views.OrderStatusViewSet)
router.register(r'orderstaxstatus', views.OrderTaxStatusViewSet)
router.register(r'privilege', views.PrivilegeViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'purchaseorderdetail', views.PurchaseOrderDetailViewSet)
router.register(r'purchaseorderstatus', views.PurchaseOrderStatusViewSet)
router.register(r'purchaseorder', views.PurchaseOrderViewSet)
router.register(r'salereport', views.SaleReportViewSet)
router.register(r'shipper', views.ShipperViewSet)
router.register(r'string', views.StringViewSet)
router.register(r'supplier', views.SupplierViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
