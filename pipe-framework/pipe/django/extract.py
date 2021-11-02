from frozendict import frozendict
from pipe.core.base import Step
from django.db.models.query import QuerySet


class EDatabaseDjango(Step):

    def __init__(self, queryset):
        self.queryset = queryset

    def get_qweryset_object(self, request):
        if not issubclass(self.queryset.__class__, QuerySet):
            raise Exception('qweryset property should be a subclass of QuerySet')

        return self.queryset

    def extract(self, request) -> frozendict:
        return self.get_qweryset_object(request)
