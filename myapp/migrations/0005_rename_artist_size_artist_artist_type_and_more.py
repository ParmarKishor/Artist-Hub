# Generated by Django 4.1.5 on 2023-01-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist_size',
            new_name='artist_type',
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_pic',
            field=models.ImageField(upload_to='artist_pic/'),
        ),
    ]
