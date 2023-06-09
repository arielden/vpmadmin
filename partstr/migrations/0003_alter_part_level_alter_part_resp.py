# Generated by Django 4.2.2 on 2023-06-18 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partstr', '0002_alter_part_level_alter_part_pntype_alter_part_resp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partstr.level'),
        ),
        migrations.AlterField(
            model_name='part',
            name='resp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
