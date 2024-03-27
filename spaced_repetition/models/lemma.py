from django.db import models
from .language import Language


class Lemma(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    citation_form = models.CharField(max_length=32)
    translation = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.language.name} lemma {self.citation_form} \"{self.translation}\""

    def to_json(self):
        return {
            "language_id": self.language_id,
            "citation_form": self.citation_form,
            "translation": self.translation,
        }
