"""
Django models for Impeachment app.

Generated by 'kawe-henrique'
date_create: 21/03/2023

this model has the function of creating a Impeachment.
"""

from django.db import models


class Impeachment(models.Model):
    """
    models:
    'id': Identification number,generated automatically.
    'company_id': company identification number.
    'name_impeachment': impeachment name.
    description_impeachment': description of impeachment.
    """

    id = models.AutoField(primary_key=True,)
    company_id = models.IntegerField(verbose_name="company_id")
    name_impeachment = models.CharField(max_length=60, null=True, verbose_name="Nome da impugnação", db_column="name_impeachment")
    description_impeachment = models.TextField(null=True,verbose_name="Descrição da impugnação",db_column="description_impeachment")

    class Meta:
        """Defining the class name within the database"""
        db_table = "impeachments"
