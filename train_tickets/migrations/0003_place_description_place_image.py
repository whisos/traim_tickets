# Generated by Django 5.0.2 on 2024-03-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_tickets', '0002_rename_user_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
    ]
