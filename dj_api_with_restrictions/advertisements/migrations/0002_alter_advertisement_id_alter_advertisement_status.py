# Generated by Django 4.2.7 on 2023-11-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[('OPEN', 'Открыто'), ('CLOSED', 'Закрыто'), ('DRAFT', 'Черновик')], default='OPEN'),
        ),
    ]
