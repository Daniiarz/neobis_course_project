# Generated by Django 2.2.6 on 2019-11-13 15:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191109_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('4309f542-683a-4a0d-b287-1287a33762ed'), editable=False),
        ),
    ]