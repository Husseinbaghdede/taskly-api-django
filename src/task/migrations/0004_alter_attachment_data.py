# Generated by Django 4.2.6 on 2023-12-18 21:04

from django.db import migrations, models
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_attachment_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='data',
            field=models.FileField(upload_to=task.models.GenerateAttachmentFilePath.__call__),
        ),
    ]
