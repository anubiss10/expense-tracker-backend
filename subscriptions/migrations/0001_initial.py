# Generated by Django 5.1.4 on 2024-12-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('recurring', models.BooleanField(default=True)),
                ('interval', models.CharField(choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=20)),
            ],
        ),
    ]
