# Generated by Django 4.2.5 on 2023-09-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='vendor/')),
                ('address', models.TextField()),
                ('mobile', models.CharField(max_length=10)),
                ('status', models.BinaryField(default=False)),
            ],
        ),
    ]
