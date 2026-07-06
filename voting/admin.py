from django.contrib import admin
from .models import Candidate, Vote, MachineState


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_marathi', 'vote_count', 'created_at']
    search_fields = ['name', 'name_marathi']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'vote_date', 'vote_time', 'timestamp']
    list_filter = ['vote_date']
    search_fields = ['candidate__name']


@admin.register(MachineState)
class MachineStateAdmin(admin.ModelAdmin):
    list_display = ['is_locked', 'total_students', 'updated_at']
