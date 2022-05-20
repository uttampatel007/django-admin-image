from django.db import models


class DemoModel(models.Model):
    title = models.CharField(max_length=122)
    image = models.ImageField(
        upload_to="demo",
        null=False,
        blank=False,
        help_text="Image size must be 1080px"
    )

    def __str__(self):
        return self.title
