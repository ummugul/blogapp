# Generated by Django 4.0.3 on 2023-12-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='categories',
        ),
        migrations.AddField(
            model_name='education',
            name='categories',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
