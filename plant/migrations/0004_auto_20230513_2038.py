# Generated by Django 3.2 on 2023-05-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0003_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='reference_photo',
            field=models.ImageField(blank=True, upload_to='request/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='angry_emo',
            field=models.ImageField(null=True, upload_to='character/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='basic_emo',
            field=models.ImageField(null=True, upload_to='character/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='happy_emo',
            field=models.ImageField(null=True, upload_to='character/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='sad_emo',
            field=models.ImageField(null=True, upload_to='character/'),
        ),
    ]
