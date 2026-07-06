from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    name_marathi = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='candidates/', blank=True, null=True)
    vote_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return '/static/images/default_avatar.jpg'


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    vote_date = models.DateField(auto_now_add=True)
    vote_time = models.TimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Vote for {self.candidate.name} at {self.vote_time}"


class MachineState(models.Model):
    is_locked = models.BooleanField(default=False)
    total_students = models.PositiveIntegerField(default=800)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Machine State"

    def __str__(self):
        return "LOCKED" if self.is_locked else "READY"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
