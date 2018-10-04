# Generated by Django 2.0.8 on 2018-10-04 08:17

from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180919_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='cost_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('GBP', 'GBP £')], default='GBP', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='miles',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='price_per_litre',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=3, default=None, default_currency='GBP', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='price_per_litre_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('GBP', 'GBP £')], default='GBP', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='cost_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('GBP', 'GBP £')], default='GBP', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('GBP', 'GBP £')], default='GBP', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='cost_of_purchase_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('GBP', 'GBP £')], default='GBP', editable=False, max_length=3),
        ),
    ]