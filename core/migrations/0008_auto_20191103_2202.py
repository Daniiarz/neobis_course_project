# Generated by Django 2.2.6 on 2019-11-03 16:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191030_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('509e44c7-b199-49b1-8ccf-bbf0b9a0ce87'), editable=False),
        ),
    ]