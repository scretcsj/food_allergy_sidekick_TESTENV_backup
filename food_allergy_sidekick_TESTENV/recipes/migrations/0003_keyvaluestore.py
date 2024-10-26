# Generated by Django 5.1.2 on 2024-10-26 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValueStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmeal', models.IntegerField(blank=True, db_column='idMeal', null=True)),
                ('strmeal', models.TextField(blank=True, db_column='strMeal', null=True)),
                ('strcategory', models.TextField(blank=True, db_column='strCategory', null=True)),
                ('strarea', models.TextField(blank=True, db_column='strArea', null=True)),
                ('strinstructions', models.TextField(blank=True, db_column='strInstructions', null=True)),
                ('strmealthumb', models.TextField(blank=True, db_column='strMealThumb', null=True)),
                ('strtags', models.TextField(blank=True, db_column='strTags', null=True)),
                ('stryoutube', models.TextField(blank=True, db_column='strYoutube', null=True)),
                ('stringredient1', models.TextField(blank=True, db_column='strIngredient1', null=True)),
                ('stringredient2', models.TextField(blank=True, db_column='strIngredient2', null=True)),
                ('stringredient3', models.TextField(blank=True, db_column='strIngredient3', null=True)),
                ('stringredient4', models.TextField(blank=True, db_column='strIngredient4', null=True)),
                ('stringredient5', models.TextField(blank=True, db_column='strIngredient5', null=True)),
                ('stringredient6', models.TextField(blank=True, db_column='strIngredient6', null=True)),
                ('stringredient7', models.TextField(blank=True, db_column='strIngredient7', null=True)),
                ('stringredient8', models.TextField(blank=True, db_column='strIngredient8', null=True)),
                ('stringredient9', models.TextField(blank=True, db_column='strIngredient9', null=True)),
                ('stringredient10', models.TextField(blank=True, db_column='strIngredient10', null=True)),
                ('stringredient11', models.TextField(blank=True, db_column='strIngredient11', null=True)),
                ('stringredient12', models.TextField(blank=True, db_column='strIngredient12', null=True)),
                ('stringredient13', models.TextField(blank=True, db_column='strIngredient13', null=True)),
                ('stringredient14', models.TextField(blank=True, db_column='strIngredient14', null=True)),
                ('stringredient15', models.TextField(blank=True, db_column='strIngredient15', null=True)),
                ('stringredient16', models.TextField(blank=True, db_column='strIngredient16', null=True)),
                ('stringredient17', models.TextField(blank=True, db_column='strIngredient17', null=True)),
                ('stringredient18', models.TextField(blank=True, db_column='strIngredient18', null=True)),
                ('stringredient19', models.TextField(blank=True, db_column='strIngredient19', null=True)),
                ('stringredient20', models.TextField(blank=True, db_column='strIngredient20', null=True)),
                ('strmeasure1', models.TextField(blank=True, db_column='strMeasure1', null=True)),
                ('strmeasure2', models.TextField(blank=True, db_column='strMeasure2', null=True)),
                ('strmeasure3', models.TextField(blank=True, db_column='strMeasure3', null=True)),
                ('strmeasure4', models.TextField(blank=True, db_column='strMeasure4', null=True)),
                ('strmeasure5', models.TextField(blank=True, db_column='strMeasure5', null=True)),
                ('strmeasure6', models.TextField(blank=True, db_column='strMeasure6', null=True)),
                ('strmeasure7', models.TextField(blank=True, db_column='strMeasure7', null=True)),
                ('strmeasure8', models.TextField(blank=True, db_column='strMeasure8', null=True)),
                ('strmeasure9', models.TextField(blank=True, db_column='strMeasure9', null=True)),
                ('strmeasure10', models.TextField(blank=True, db_column='strMeasure10', null=True)),
                ('strmeasure11', models.TextField(blank=True, db_column='strMeasure11', null=True)),
                ('strmeasure12', models.TextField(blank=True, db_column='strMeasure12', null=True)),
                ('strmeasure13', models.TextField(blank=True, db_column='strMeasure13', null=True)),
                ('strmeasure14', models.TextField(blank=True, db_column='strMeasure14', null=True)),
                ('strmeasure15', models.TextField(blank=True, db_column='strMeasure15', null=True)),
                ('strmeasure16', models.TextField(blank=True, db_column='strMeasure16', null=True)),
                ('strmeasure17', models.TextField(blank=True, db_column='strMeasure17', null=True)),
                ('strmeasure18', models.TextField(blank=True, db_column='strMeasure18', null=True)),
                ('strmeasure19', models.TextField(blank=True, db_column='strMeasure19', null=True)),
                ('strmeasure20', models.TextField(blank=True, db_column='strMeasure20', null=True)),
                ('strsource', models.TextField(blank=True, db_column='strSource', null=True)),
            ],
            options={
                'db_table': 'key_value_store',
                'managed': False,
            },
        ),
    ]
