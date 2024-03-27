from django.contrib import admin
from django.urls import include, path, re_path

from .views.languages import LanguagesView
from .views.react_index import ReactIndexView
from .views.current_user_state import CurrentUserStateView
from .views.choose_language import ChooseLanguageView
from .views.submit_document import SubmitDocumentView
from .views.document import DocumentView
from .views.documents import DocumentsView
from .views.words_in_sentence import WordsInSentenceView
from .views.search_lemmas import SearchLemmasView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "google_sso/",
        include("django_google_sso.urls", namespace="django_google_sso")
    ),

    path(
        "api/current_user_state",
        CurrentUserStateView.as_view(),
        name="current_user_state",
    ),
    path("api/choose_language", ChooseLanguageView.as_view(), name="choose_language"),
    path("api/languages", LanguagesView.as_view(), name="languages"),
    path("api/submit_document", SubmitDocumentView.as_view(), name="submit_document"),
    path("api/document/<int:document_id>", DocumentView.as_view(), name="document"),
    path("api/documents", DocumentsView.as_view(), name="document"),
    path("api/words_in_sentence", WordsInSentenceView.as_view(), name="words_in_sentence"),
    path("api/search_lemmas", SearchLemmasView.as_view(), name="search_lemmas"),

    re_path(r'^.*$', ReactIndexView.as_view(), name="react_index")
]
