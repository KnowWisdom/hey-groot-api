# Generated by Django 3.2 on 2023-05-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0006_auto_20230516_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
