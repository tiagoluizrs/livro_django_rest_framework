from django.urls import include, path
from rest_framework import routers
from productManager.views import (
    MyTokenObtainPairView,
    ProductView,
    ClientView,
    EntryOutputView,
    HistoryEntryOutputView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    ProductExportCSVView,
)
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register(r"product", ProductView)
router.register(r"client", ClientView)
router.register(r"entry-out-put", EntryOutputView)
router.register(r"history-entry-out-put", HistoryEntryOutputView)

urlpatterns = [
    path("", include(router.urls)),
    # Mova as rotas abaixo para dentro desse arquivo, retirando-as do arquivo  `productManagerAdmin\urls.py`
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("category/", CategoryListCreateView.as_view(), name="category-list-create"),
    path(
        "category/<int:pk>/",
        CategoryRetrieveUpdateDestroyView.as_view(),
        name="category-detail-update-delete",
    ),
    path("products/export-csv/", ProductExportCSVView.as_view(), name="product-export"),
]
