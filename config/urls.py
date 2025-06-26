from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from hotel.views import (
    EnderecoViewSet, HospedeViewSet, QuartoViewSet, ReservaViewSet,
    ServicoViewSet, ReservaServicoViewSet, PagamentoViewSet, FuncionarioViewSet
)

router = DefaultRouter()
router.register(r'enderecos', EnderecoViewSet)
router.register(r'hospedes', HospedeViewSet)
router.register(r'quartos', QuartoViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'reservaservicos', ReservaServicoViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]