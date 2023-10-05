# Generated by Django 4.2.6 on 2023-10-05 08:41

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ingridient_recipe_ingridients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingridient',
            new_name='Ingredient',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='ingridients',
            new_name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]