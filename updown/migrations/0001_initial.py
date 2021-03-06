# Generated by Django 3.0.8 on 2020-07-28 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import updown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('사진', models.ImageField(upload_to=updown.models.uploadpath)),
                ('content', models.CharField(max_length=100)),
                ('postdate', models.DateField(auto_now_add=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('사용자', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
