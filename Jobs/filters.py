import django_filters
from django.db.models import Q
from django import forms

import Jobs
from Jobs.models import Reg, Job


class RecruiterFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search',widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Reg
        fields = ['search']
    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(mobile__icontains=value) |
            Q(email__icontains=value) |
            Q(address=value)
        )

class JobSeekerFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search',widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Reg
        fields = ['search']
    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(mobile__icontains=value) |
            Q(email__icontains=value) |
            Q(address=value)
        )

class JobsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 150px; text-align: center;margin: 0 auto;'}))

    class Meta:
        model = Job
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(company__icontains=value) |
            Q(location__icontains=value) |
            Q(type__icontains=value)
        )