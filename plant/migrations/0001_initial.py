# Generated by Django 3.2 on 2023-05-11 17:59

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('basic_emo', models.ImageField(null=True, upload_to='appname')),
                ('angry_emo', models.ImageField(null=True, upload_to='appname')),
                ('sad_emo', models.ImageField(null=True, upload_to='appname')),
                ('happy_emo', models.ImageField(null=True, upload_to='appname')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_alarm', models.BooleanField(default=True)),
                ('pot_color', colorfield.fields.ColorField(default='##f5c542', image_field=None, max_length=18, samples=None)),
                ('character_id', models.ForeignKey(db_column='character_id', on_delete=django.db.models.deletion.CASCADE, related_name='character', to='plant.character')),
            ],
        ),
    ]
