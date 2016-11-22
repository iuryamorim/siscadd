from django.db import models


class Report(models.Model):

    def file_path(self, filmename):
        rota = ""