# Generated by Django 3.2.4 on 2021-06-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_pedido', '0003_itempedido_rentabilidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
