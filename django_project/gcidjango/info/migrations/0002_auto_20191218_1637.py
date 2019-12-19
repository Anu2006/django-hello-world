# Generated by Django 3.0 on 2019-12-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('school', models.CharField(blank=True, max_length=200)),
                ('over_18', models.BooleanField(verbose_name=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]