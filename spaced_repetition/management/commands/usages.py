from django.core.management.base import BaseCommand
from spaced_repetition.models.language import LANGUAGE_IDS
from spaced_repetition.models.word_in_sentence import WordInSentence
from spaced_repetition.views.search_lemmas import get_search_results


class Command(BaseCommand):
    help = 'Search for words based on a search string'

    def add_arguments(self, parser):
        parser.add_argument("lemma_id")

    def handle(self, *args, **options):
        words = WordInSentence.objects.filter(lemma_id=options["lemma_id"]).select_related("sentence").prefetch_related("substrings")
        for word in words:
            print(f"https://membaca-b8789e9ca984.herokuapp.com/document/{word.sentence.document_id}")

            text = word.sentence.text
            for substring in sorted(list(word.substrings.all()), key=lambda s: -s.start):
                text = text[:substring.start] + "<" + text[substring.start:substring.end] + ">" + text[substring.end:]

            print(text)
            print()
