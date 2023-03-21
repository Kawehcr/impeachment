from django.db import models

class Impeachment(models.Model):
    id = models.AutoField(primary_key=True,)
    company_id = models.IntegerField(verbose_name="company_id")
    name_impeachment = models.CharField(max_length=60, null=True, verbose_name="Nome da impugnação", db_column="name_impeachment")
    description_impeachment = models.CharField(max_length=100,null=True,verbose_name="Descrição da impugnação",db_column="description_impeachment")

    class Meta:
        db_table = "Impeachment"
