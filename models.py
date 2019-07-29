from django.db import models

class sign_up(models.Model):
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=20)
    emailid=models.EmailField(unique=True)
    address=models.CharField(max_length=300)

    class Meta:
        db_table='sign_up_credentials'