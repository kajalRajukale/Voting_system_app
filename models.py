from django.db import models
from django.core.validators import RegexValidator


class Candidate(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='candidates/photos/', blank=True, null=True)
    symbol = models.ImageField(upload_to='candidates/symbols/', blank=True, null=True)
    party = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.position})"

    @property
    def total_votes(self):
        return self.votes.count()


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    voter_id = models.CharField(max_length=100, unique=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    browser = models.CharField(max_length=200, blank=True, null=True)
    operating_system = models.CharField(max_length=100, blank=True, null=True)
    device = models.CharField(max_length=100, blank=True, null=True)
    vote_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-vote_time']

    def __str__(self):
        return f"{self.voter_id} voted for {self.candidate.name}"
