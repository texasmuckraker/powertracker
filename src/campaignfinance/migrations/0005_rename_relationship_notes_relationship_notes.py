# Generated by Django 4.2.2 on 2023-06-20 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaignfinance', '0004_remove_document_campaign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='relationship_notes',
            new_name='notes',
        ),
    ]
