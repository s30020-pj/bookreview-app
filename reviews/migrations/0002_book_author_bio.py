# Generated by Django 5.1.6 on 2025-02-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_bio',
            field=models.TextField(default='Test author bio'),
            preserve_default=False,
        ),
    ]
