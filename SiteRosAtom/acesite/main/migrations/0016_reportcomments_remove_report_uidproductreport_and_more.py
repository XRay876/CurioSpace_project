# Generated by Django 4.2.2 on 2023-07-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_report_udatereport_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uProductIDReport', models.CharField(max_length=50, verbose_name='ID Продукта')),
                ('uVehIDReport', models.CharField(max_length=50, verbose_name='ID Вехи')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.RemoveField(
            model_name='report',
            name='uIDProductReport',
        ),
        migrations.RemoveField(
            model_name='report',
            name='uIDVehReport',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
