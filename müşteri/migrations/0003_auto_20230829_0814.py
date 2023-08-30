# Generated by Django 3.2.7 on 2023-08-29 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('müşteri', '0002_auto_20230828_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(max_length=60, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='müşteri.date'),
        ),
    ]
