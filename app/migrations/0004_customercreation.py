# Generated by Django 2.2.20 on 2021-05-12 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20210511_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customercreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('priority', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]