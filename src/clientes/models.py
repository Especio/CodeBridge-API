from django.db import models

class Cliente(models.Model):

    ESTADOS = [
        ("SP", "São Paulo"),
        ("MG", "Minas Gerais"),
        ("GO", "Goiás")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    cidade = models.CharField(max_length=70, null=False, blank=False)
    estado = models.CharField(choices=ESTADOS, max_length=2, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=True, blank=True)

    #para representar essa instancial como o nome do cliente.
    def __str__(self):
        return self.nome
        #return f"{self.nome} - {self.cidade}"