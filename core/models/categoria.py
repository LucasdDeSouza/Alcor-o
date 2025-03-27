from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição', help_text='Descrição da categoria')