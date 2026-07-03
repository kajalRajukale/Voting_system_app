from django.contrib import admin
from .models import Candidate, Vote


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'party', 'position', 'status', 'created_at']
    list_filter = ['status', 'position']
    search_fields = ['name', 'party', 'position']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['voter_id', 'candidate', 'ip_address', 'vote_time']
    list_filter = ['vote_time']
    search_fields = ['voter_id', 'candidate__name']
