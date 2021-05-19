# Generated by Django 3.2.2 on 2021-05-13 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco_tabela', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('multiplo', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]