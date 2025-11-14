import django_filters
from .models import Proposal, status, proposal_type


class ProposalFilter(django_filters.FilterSet):
    status = django_filters.MultipleChoiceFilter(choices=status)
    type = django_filters.MultipleChoiceFilter(choices=proposal_type)
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Proposal
        fields = ['status', 'type', 'created_at', 'updated_at']

