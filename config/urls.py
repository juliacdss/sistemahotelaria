from rest_framework.viewsets import ModelViewSet
from .models import Endereco, Hospede, Quarto, Reserva, Servico, ReservaServico, Pagamento, Funcionario
from .serializers import EnderecoSerializer, HospedeSerializer, QuartoSerializer, ReservaSerializer, ServicoSerializer, ReservaServicoSerializer, PagamentoSerializer, FuncionarioSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class HospedeViewSet(ModelViewSet):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer    

class QuartoViewSet(ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer    

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer    

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class ReservaServicoViewSet(ModelViewSet):
    queryset = ReservaServico.objects.all()
    serializer_class = ReservaServicoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer    

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer    