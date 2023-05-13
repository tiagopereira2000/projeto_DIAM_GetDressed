# Generated by Django 4.1.7 on 2023-05-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_alter_client_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='sizes',
            field=models.ManyToManyField(to='WebApp.size'),
        ),
    ]
