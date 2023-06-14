# Generated by Django 4.2.1 on 2023-06-12 12:50

import app.service.service
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, choices=[('CHUI', 'CHUI'), ('DJALAL-ABAD', 'DJALAL-ABAD'), ('OSH', 'OSH'), ('NARYN', 'NARYN'), ('TALAS', 'TALAS'), ('ISSYK-KUL', 'ISSYK-KUL')], max_length=300, verbose_name='region')),
                ('street', models.CharField(max_length=50, verbose_name='street')),
                ('apartment', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storey', models.CharField(blank=True, choices=[('Bungalow', 'Bungalow'), ('Duplex', 'Duplex'), ('One Storeys', 'One Storeys'), ('Two Storeys', 'Two Storeys'), ('Three Storeys', 'Three Storeys'), ('Four Storeys', 'Four Storeys'), ('Five Storeys', 'Five Storeys')], max_length=300, verbose_name='storey')),
                ('bedroom', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=300, unique=True, verbose_name='bed')),
                ('bathroom', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=300, verbose_name='bathroom')),
                ('furnished', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no'), ('somewhat', 'somewhat')], max_length=300, verbose_name='furnished')),
                ('parking_space', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=300, verbose_name='parking_space')),
                ('new_property', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=300, verbose_name='new_property')),
                ('purpose', models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Office', 'Office'), ('Business', 'Business'), ('Other', 'Other')], max_length=300, unique=True, verbose_name='porpose')),
                ('duration', models.CharField(blank=True, choices=[('1 month', '1 month'), ('3 months', '3 months'), ('6 months', '6 months'), ('Year', 'Year'), ('2 Years', '2 Years'), ('3 Years', '3 Years')], max_length=300, verbose_name='duration')),
                ('square_meter', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20)),
                ('featrued', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=100)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='property.address', verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Property',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to=app.service.service.upload_image_path)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_id', to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_choices', models.CharField(choices=[('rent', 'Rent'), ('sale', 'Sale'), ('term', 'Term')], max_length=10, verbose_name='deal')),
                ('currency_choices', models.CharField(choices=[('ru', 'RU'), ('us', 'US'), ('som', 'SOM'), ('ero', 'ERO')], max_length=10, verbose_name='currency')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateField()),
                ('additional_info', models.TextField()),
                ('feedback', models.ManyToManyField(to='property.feedback')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='property.city', verbose_name='City'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='property.district', verbose_name='District'),
        ),
    ]
