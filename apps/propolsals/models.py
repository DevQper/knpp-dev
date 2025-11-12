from django.db import models

# Create your models here.

proposal_type = [
    ('product-enchancement', 'Product Enchancement'),
    ('process-optimization', 'Process Optimization'),
    ('user-experience', 'User Experience'),
    ('cost-reduction', 'Cost Reduction'),
    ('other', 'Other'),
]

status = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
    ('pilot', 'Pilot'),
]

class Proposal(models.Model):
    proposed_by = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=255)
    file = models.FileField(upload_to='proposals/', null=True, blank=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=proposal_type, default='other')
    status = models.CharField(max_length=255, choices=status, default='pending')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title