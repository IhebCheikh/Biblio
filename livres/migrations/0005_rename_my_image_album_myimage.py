# Generated by Django 5.1.3 on 2024-11-28 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livres', '0004_alter_album_my_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='my_image',
            new_name='myimage',
        ),
    ]
