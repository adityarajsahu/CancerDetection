# Generated by Django 4.1.3 on 2023-03-10 17:46

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
            name='breastImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xrayImage', models.ImageField(upload_to='xrayImages/')),
                ('uploadedOn', models.DateTimeField(auto_now_add=True)),
                ('maskImage', models.ImageField(upload_to='segmentedImages/')),
                ('uploadedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]