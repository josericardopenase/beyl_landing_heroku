# Generated by Django 3.1.2 on 2020-12-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0025_auto_20201213_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='emails',
            name='name',
            field=models.CharField(default='paco', max_length=255),
            preserve_default=False,
        ),
    ]