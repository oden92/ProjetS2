# Generated by Django 5.0.4 on 2024-05-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0009_remove_livre_created_at_remove_livre_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='lien',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
