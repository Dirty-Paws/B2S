# Generated by Django 3.1.2 on 2020-10-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlAPI', '0003_auto_20201014_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodremainingtimes',
            name='Food_Amount_gr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodremainingtimes',
            name='Location_Id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodremainingtimes',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodremainingtimes',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]