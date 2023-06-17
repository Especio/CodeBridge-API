from django.db import models

class Conta(models.Model):
    cliente = models.ForeignKey("clientes.Cliente", 
                                null=True,
                                on_delete=models.SET_NULL,
                                related_name="contas")

    saldo = models.DecimalField("saldo do cliente",
                                max_digits=12,
                                decimal_places=2,
                                default=0)
    data_abertura = models.DateTimeField(auto_now=True, null=False)

    def depositar(self, valor):
        self.saldo += valor
        self.save() #no banco
    
    def debitar(self, valor):
        self.saldo -= valor
        self.save() #no banco


    def __str__(self):
        return f"{self.cliente} - {self.saldo}"