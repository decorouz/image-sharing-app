# Generated by Django 4.0.2 on 2022-02-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_users_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveBigIntegerField(db_index=True, default=0),
        ),
    ]
