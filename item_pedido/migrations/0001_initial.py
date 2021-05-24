# Generated by Django 3.2.3 on 2021-05-24 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_multiplo', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('produto_nome', models.CharField(max_length=100)),
                ('produto_preco_tabela', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_liquido', models.DecimalField(decimal_places=2, max_digits=12)),
                ('rentabilidade_produto', models.IntegerField(blank=True, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pedidos.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produtos.produto')),
            ],
        ),
    ]
