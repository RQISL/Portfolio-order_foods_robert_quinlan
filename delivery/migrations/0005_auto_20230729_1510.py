# Generated by Django 3.2.20 on 2023-07-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_remove_menuitem_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='county',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='eirecode',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
