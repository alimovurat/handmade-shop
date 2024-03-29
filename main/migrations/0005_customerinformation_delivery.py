# Generated by Django 5.0.2 on 2024-03-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_product_attributes_product_baguette_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('apartment', models.IntegerField(default=0)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=20)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('russia_curier_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('nab_chelny_curier_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('pickup', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name': 'delivery',
                'verbose_name_plural': 'deliveries',
            },
        ),
    ]
