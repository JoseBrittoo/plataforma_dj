from django.db import models

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    quantidade_modulos = models.IntegerField()
    nivel = models.CharField(max_length=20)
    descricao = models.TextField()
    total_horas = models.IntegerField()
    nome_proprietario = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nome_curso

class Modulo(models.Model):
    nome_curso = models.CharField(max_length=100)
    conteudo = models.TextField()
    curso = models.ForeignKey(Curso, related_name='modulos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_curso

