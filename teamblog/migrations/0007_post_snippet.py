# Generated by Django 3.2.4 on 2021-06-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamblog', '0006_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above to Read the Blog Post.', max_length=255),
        ),
    ]
