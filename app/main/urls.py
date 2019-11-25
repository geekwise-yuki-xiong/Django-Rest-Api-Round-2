# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from drf import views as drf_views
from bank import views as bank_views

router = routers.DefaultRouter()
router.register(r'users', drf_views.UserViewSet)
router.register(r'groups', drf_views.GroupViewSet)
router.register(r'bank/branch', bank_views.BranchViewSet)
router.register(r'bank/account', bank_views.AccountViewSet)
router.register(r'bank/customer', bank_views.CustomerViewSet)
router.register(r'bank/product', bank_views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('bank/branch/create', bank_views.branch_create, name='branch_create'),
    path('bank/branch/read', bank_views.branch_read, name='branch_read'),
]
