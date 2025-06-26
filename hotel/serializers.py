from rest_framework.serializers import ModelSerializer
from .models import Endereco, Hospede, Quarto, Reserva, Servico, ReservaServico, Pagamento, Funcionario

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__' 

class HospedeSerializer(ModelSerializer):
    class Meta:
        model = Hospede
        fields = '__all__' 

class QuartoSerializer(ModelSerializer):
    class Meta:
        model = Quarto
        fields = '__all__'        

class ReservaSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'   

class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'           

class ReservaServicoSerializer(ModelSerializer):
    class Meta:
        model = ReservaServico
        fields = '__all__'     

class PagamentoSerializer(ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'                 

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'   git push -u origin feature/serializer
