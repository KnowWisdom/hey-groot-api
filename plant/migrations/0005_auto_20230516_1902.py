# Generated by Django 3.2 on 2023-05-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0004_auto_20230513_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='angry_emo',
            field=models.ImageField(blank=True, null=True, upload_to='character/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='basic_emo',
            field=models.ImageField(blank=True, null=True, upload_to='character/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='happy_emo',
            field=models.ImageField(blank=True, null=True, upload_to='character/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='sad_emo',
            field=models.ImageField(blank=True, null=True, upload_to='character/'),
        ),
    ]