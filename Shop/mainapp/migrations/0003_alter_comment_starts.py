# Generated by Django 4.2.2 on 2023-07-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_book_author_alter_comment_starts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='starts',
            field=models.CharField(choices=[('4', '4'), ('1', '1'), ('5', '5'), ('3', '3'), ('2', '2')], default='1', max_length=20),
        ),
    ]