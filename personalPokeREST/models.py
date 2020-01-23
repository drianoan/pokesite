from django.db import models

# Create your models here.
class pokemonManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(identifier=name)

class pokemon (models.Model):
    id = models.IntegerField(blank=True,null=False,primary_key=True)
    identifier = models.CharField(blank=True,max_length=200)
    species_id = models.IntegerField(blank=True,null=True)
    height = models.IntegerField(blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    base_experience = models.IntegerField(blank=True,null=True)
    order = models.IntegerField(blank=True,null=True)
    is_default = models.IntegerField(blank=True,null=True)
    
    objects = pokemonManager()

    def __str__(self):
        return self.identifier

class pokemon_speciesManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(identifier=name)

class pokemon_species (models.Model):
    id = models.IntegerField(blank=True,null=False,primary_key=True)
    identifier = models.CharField(blank=True,max_length=200)
    generation_id = models.IntegerField(blank=True,null=True)
    evolves_from_species_id = models.CharField(blank=True,max_length=200)
    evolution_chain_id = models.IntegerField(blank=True,null=True)
    color_id = models.IntegerField(blank=True,null=True)
    shape_id = models.IntegerField(blank=True,null=True)
    habitat_id = models.IntegerField(blank=True,null=True)
    gender_rate = models.IntegerField(blank=True,null=True)
    capture_rate = models.IntegerField(blank=True,null=True)
    base_happiness = models.IntegerField(blank=True,null=True)
    is_baby = models.IntegerField(blank=True,null=True)
    hatch_counter = models.IntegerField(blank=True,null=True)
    has_gender_differences = models.IntegerField(blank=True,null=True)
    growth_rate_id = models.IntegerField(blank=True,null=True)
    forms_switchable = models.IntegerField(blank=True,null=True)
    order = models.IntegerField(blank=True,null=True)
    conquest_order = models.CharField(blank=True,max_length=200)

    objects = pokemon_speciesManager()

    def __str__(self):
        return self.identifier

