# Generated by Django 5.2.3 on 2025-06-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Branch name:'),
        ),
    ]
