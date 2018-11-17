# Generated by Django 2.1.3 on 2018-11-15 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, verbose_name='URLS')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creater')),
            ],
            options={
                'verbose_name': 'Link status',
                'verbose_name_plural': 'Links status',
            },
        ),
    ]