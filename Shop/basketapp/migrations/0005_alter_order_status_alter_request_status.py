# Generated by Django 4.2.2 on 2023-08-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0004_alter_order_status_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Готов к отгрузке', 'Готов к отгрузке'), ('Ожидает', 'Ожидает'), ('В обработке', 'В обработке'), ('Закрыт', 'Закрыт')], default='Ожидает', max_length=20),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Готов к отгрузке', 'Готов к отгрузке'), ('Ожидает', 'Ожидает'), ('В обработке', 'В обработке'), ('Закрыт', 'Закрыт')], default='Ожидает', max_length=20),
        ),
    ]
