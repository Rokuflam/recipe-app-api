# Generated by Django 4.2.5 on 2023-09-27 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tag_recipe_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingridient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingridients',
            field=models.ManyToManyField(to='core.ingridient'),
        ),
    ]
