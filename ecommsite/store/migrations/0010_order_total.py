# Generated by Django 3.2.5 on 2021-07-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_item_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
