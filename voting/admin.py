from django.contrib import admin
from .models import Symbol, Vote, MachineState


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    list_display = ['name', 'vote_count', 'created_at']
    search_fields = ['name']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'vote_date', 'vote_time', 'timestamp']
    list_filter = ['vote_date']
    search_fields = ['symbol__name']


@admin.register(MachineState)
class MachineStateAdmin(admin.ModelAdmin):
    list_display = ['is_locked', 'total_students', 'updated_at']
