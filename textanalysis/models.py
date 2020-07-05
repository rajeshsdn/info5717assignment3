from django.db import models

class WFreq(models.Model):
    wordid = models.AutoField(primary_key=True)
    word = models.CharField(max_length=45,null=False)
    frequency = models.CharField(max_length=5,null=False)

    class Meta:
        db_table='wfreq'
