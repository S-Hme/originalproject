# Generated by Django 4.0.1 on 2022-06-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_like_post_alter_like_user_likeprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='postrecruit',
            name='praTime',
            field=models.TextField(default=1, max_length=300, verbose_name='練習時間帯'),
            preserve_default=False,
        ),
    ]
