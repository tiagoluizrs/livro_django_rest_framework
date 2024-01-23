from django.urls import include, path
from rest_framework import routers
from productManager.views import MyTokenObtainPairView, ProductView, CategoryView, ClientView, EntryOutputView, HistoryEntryOutputView

router = routers.DefaultRouter()
router.register(r'product', ProductView)
router.register(r'category', CategoryView)
router.register(r'client', ClientView)
router.register(r'entry-out-put', EntryOutputView)
router.register(r'history-entry-out-put', HistoryEntryOutputView)

urlpatterns = [
    path("", include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
