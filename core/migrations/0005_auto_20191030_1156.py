# Generated by Django 2.2.6 on 2019-10-30 05:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191030_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('2bfc7b0d-2116-4561-9237-a77b3f863d99'), editable=False),
        ),
    ]
