# Generated by Django 4.2.2 on 2023-07-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0003_alter_basket_status_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='status',
            field=models.CharField(choices=[('Закрыт', 'Закрыт'), ('Готов к отгрузке', 'Готов к отгрузке'), ('Ожидает', 'Ожидает'), ('В обработке', 'В обработке')], default='Ожидает', max_length=20),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Закрыт', 'Закрыт'), ('Готов к отгрузке', 'Готов к отгрузке'), ('Ожидает', 'Ожидает'), ('В обработке', 'В обработке')], default='Ожидает', max_length=20),
        ),
    ]
