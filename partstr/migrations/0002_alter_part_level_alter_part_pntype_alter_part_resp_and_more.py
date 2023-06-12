# Generated by Django 4.2.2 on 2023-06-12 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partstr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='level',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partstr.level'),
        ),
        migrations.AlterField(
            model_name='part',
            name='pntype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partstr.pntype'),
        ),
        migrations.AlterField(
            model_name='part',
            name='resp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='part',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partstr.status'),
        ),
    ]