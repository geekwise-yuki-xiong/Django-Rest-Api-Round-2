# Generated by Django 2.2.7 on 2019-11-27 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bank_partner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer_bank_partner', to='bank.Branch'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_bank_partner', to='bank.Branch'),
        ),
    ]
