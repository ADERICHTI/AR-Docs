# Generated by Django 5.1.4 on 2025-01-13 09:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_doc_content_alter_document_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
