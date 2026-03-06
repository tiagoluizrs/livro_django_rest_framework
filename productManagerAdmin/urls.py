from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# Adicione o response apenas para teste
from django.http import HttpResponse


# Adicione esse método apenas para teste
def trigger_error(request):
    division_by_zero = 1 / 0
    return HttpResponse("Isso nunca será exibido")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("productManager.urls")),
    # Rota para baixar o arquivo do Schema (YAML/JSON)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Rota para a interface gráfica SWAGGER UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Rota para a interface gráfica REDOC (Alternativa)
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("", include("django_prometheus.urls")),
    path("sentry-debug/", trigger_error),
]
