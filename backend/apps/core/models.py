# from django.db import models
# from django.utils import timezone  # For manual timestamps if needed

# class TimeStampedModel(models.Model):  # Base: models.Model, NOT (abstract=True)
#     created_at = models.DateTimeField(auto_now_add=True)  # Auto-sets on create
#     updated_at = models.DateTimeField(auto_now=True)      # Auto-updates on save

#     class Meta:  # Here's the "abstract" flag – like a recipe note
#         abstract = True  # No DB table; inherit only

#     # Optional: Custom save for manual tweaks
#     def save(self, *args, **kwargs):
#         if not self.created_at:
#             self.created_at = timezone.now()
#         super().save(*args, **kwargs)

# class UUIDModel(models.Model):  # Bonus: For UUID PKs (secure, distributed IDs)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     class Meta:
#         abstract = True