# Generated by Django 3.2.5 on 2021-09-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name2',
        ),
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
