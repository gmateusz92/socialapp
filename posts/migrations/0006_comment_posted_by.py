# Generated by Django 4.1.1 on 2023-01-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='mateusz', max_length=100),
            preserve_default=False,
        ),
    ]
