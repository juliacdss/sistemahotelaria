from django.contrib import admin
from .models import Endereco, Hospede, Quarto, Reserva, Servico, ReservaServico, Pagamento, Funcionario

admin.site.register(Endereco)
admin.site.register(Hospede)
admin.site.register(Quarto)
admin.site.register(Reserva)
admin.site.register(Servico)
admin.site.register(ReservaServico)
admin.site.register(Pagamento)
admin.site.register(Funcionario)