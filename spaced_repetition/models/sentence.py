from django.db import models
from .document import Document


class Sentence(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    position = models.IntegerField()
    text = models.CharField(max_length=256)
    translation = models.CharField(max_length=256)
    # URL to an image that will be displayed above the sentence
    image = models.CharField(max_length=256, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_sentence_position",
                fields=[
                    "document",
                    "position",
                ],
            )
        ]

    def __str__(self):
        return self.text

    def to_json(self):
        # document and position are not expected to be included,
        # since they are usually just used for orders and joins
        return {
            "id": self.id,
            "text": self.text,
            "translation": self.translation,
            "image": self.image or None,
        }
