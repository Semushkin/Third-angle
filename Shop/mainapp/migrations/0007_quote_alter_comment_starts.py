# Generated by Django 4.2.2 on 2023-07-30 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_comment_starts_alter_news_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=64)),
                ('is_active', models.BooleanField(default=False)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='starts',
            field=models.CharField(choices=[('1', '1'), ('3', '3'), ('2', '2'), ('4', '4'), ('5', '5')], default='1', max_length=20),
        ),
    ]