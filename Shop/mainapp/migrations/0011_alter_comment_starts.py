# Generated by Django 4.2.2 on 2023-08-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_comment_starts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='starts',
            field=models.CharField(choices=[('5', '5'), ('1', '1'), ('3', '3'), ('2', '2'), ('4', '4')], default='1', max_length=20),
        ),
    ]