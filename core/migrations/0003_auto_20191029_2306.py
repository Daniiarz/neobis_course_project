# Generated by Django 2.2.6 on 2019-10-29 17:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_course_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.IntegerField(choices=[(1, 'Phone'), (2, 'Facebook'), (3, 'Email')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('ef06bf0d-ee47-429c-8cf1-d3c663f817b4'), editable=False),
        ),
    ]
