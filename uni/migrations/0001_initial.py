# Generated by Django 4.1.4 on 2022-12-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(default='a', max_length=122, null=True)),
                ('password', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
    ]
