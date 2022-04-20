# Generated by Django 4.0.1 on 2022-03-13 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_postrecruit'),
    ]

    operations = [
        migrations.AddField(
            model_name='postrecruit',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
