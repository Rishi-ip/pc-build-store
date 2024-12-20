# Generated by Django 5.1.3 on 2024-11-14 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalprice', models.FloatField(default=0.0)),
                ('cust_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='component.customer')),
                ('product_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='component.product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
