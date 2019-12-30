# Generated by Django 3.0 on 2019-12-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]