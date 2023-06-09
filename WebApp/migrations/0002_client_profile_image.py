# Generated by Django 4.1.7 on 2023-05-13 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    def set_default_profile_image(apps, schema_editor):
        Client = apps.get_model('WebApp', 'Client')
        Client.objects.filter(profile_image__isnull=True).update(profile_image='default_client.png')

    operations = [
        migrations.AddField(
            model_name='client',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='images/', default=None),
        ),
        migrations.RunPython(set_default_profile_image),
        migrations.AlterField(
            model_name='client',
            name='profile_image',
            field=models.ImageField(default='default_client.png', upload_to='images/', null=True),
        ),
    ]
