from rest_framework import serializers
from .models import Snippet # don't use `from tutorial.snippets.models import ...`, or the import of SnippetSerializer will fail [model ... doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS]


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
