# Generated by Django 4.1 on 2022-09-04 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_created_date_post_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nota',
            new_name='texto',
        ),
        migrations.RemoveField(
            model_name='post',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subtitulo',
        ),
    ]
