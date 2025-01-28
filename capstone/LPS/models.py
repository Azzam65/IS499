from django.db import models

class UserTable(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)

    class Meta:
        db_table = 'lps_usertable'  # Specify the table name

    def __str__(self):
        return self.username