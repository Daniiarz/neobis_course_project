# Generated by Django 2.2.6 on 2019-10-29 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('506e7e37-e70b-4f98-9077-3a5c212f81b4'), editable=False),
        ),
    ]