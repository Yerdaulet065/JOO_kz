# Generated by Django 4.1.7 on 2023-04-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
