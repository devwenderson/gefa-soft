from django.db import models
from app.produtos.models import Produto
# Create your models here.

class Venda(models.Model):
    data = models.DateField(verbose_name='Data da Venda')

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return f"{self.data} - R${self.valor}"

    @property
    def produtos_vendidos(self):
        return ProdutoVenda.objects.filter(venda=self)

    @property
    def valor(self):
        valor = 0
        for produto_vendido in self.produtos_vendidos:
            valor += produto_vendido.quantidade * produto_vendido.produto.preco
        return valor


class ProdutoVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.PROTECT, verbose_name='Venda')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, verbose_name='Produto')
    quantidade = models.DecimalField(verbose_name='Quantidade',max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Produto Vendido'
        verbose_name_plural = 'Produtos Vendidos'

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} {self.produto.unidade}"
    