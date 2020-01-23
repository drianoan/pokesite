# Generated by Django 3.0.2 on 2020-01-23 18:13

from django.db import migrations, models
import personalPokeREST.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pokemon',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('identifier', models.CharField(blank=True, max_length=200)),
                ('species_id', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('base_experience', models.IntegerField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('is_default', models.IntegerField(blank=True, null=True)),
            ],
            managers=[
                ('objects', personalPokeREST.models.pokemonManager()),
            ],
        ),
        migrations.CreateModel(
            name='pokemon_species',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('identifier', models.CharField(blank=True, max_length=200)),
                ('generation_id', models.IntegerField(blank=True, null=True)),
                ('evolution_chain_id', models.IntegerField(blank=True, null=True)),
                ('color_id', models.IntegerField(blank=True, null=True)),
                ('shape_id', models.IntegerField(blank=True, null=True)),
                ('habitat_id', models.IntegerField(blank=True, null=True)),
                ('gender_rate', models.IntegerField(blank=True, null=True)),
                ('capture_rate', models.IntegerField(blank=True, null=True)),
                ('base_happiness', models.IntegerField(blank=True, null=True)),
                ('is_baby', models.IntegerField(blank=True, null=True)),
                ('hatch_counter', models.IntegerField(blank=True, null=True)),
                ('has_gender_differences', models.IntegerField(blank=True, null=True)),
                ('growth_rate_id', models.IntegerField(blank=True, null=True)),
                ('forms_switchable', models.IntegerField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('conquest_order', models.CharField(blank=True, max_length=200)),
            ],
            managers=[
                ('objects', personalPokeREST.models.pokemon_speciesManager()),
            ],
        ),
    ]
