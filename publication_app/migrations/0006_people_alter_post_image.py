# Generated by Django 4.0.4 on 2022-05-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0005_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
