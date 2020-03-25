from django.db import models
from django.contrib.auth.models import User

INDCHOICES = (
    ('FINANCE', 'FINANCE'),
    ('HEALTHCARE', 'HEALTHCARE'),
    ('INSURANCE', 'INSURANCE'),
    ('LEGAL', 'LEGAL'),
    ('MANUFACTURING', 'MANUFACTURING'),
    ('PUBLISHING', 'PUBLISHING'),
    ('REAL ESTATE', 'REAL ESTATE'),
    ('SOFTWARE', 'SOFTWARE'),
)

class Account(models.Model):
    name = models.CharField(max_length=64, null = False)
    email = models.EmailField(null = False)
    phone = models.CharField(max_length=20, null = False)
    industry = models.CharField("Industry Type", max_length=255, choices=INDCHOICES, blank=True, null=False)
    website = models.URLField("Website", blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    createdBy = models.ForeignKey(User, related_name='account_created_by', on_delete=models.CASCADE)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ContactSource(models.Model):
    status = models.CharField("Contact Source", max_length=20)

    def __str__(self):
        return self.status

class ContactStatus(models.Model):
    status = models.CharField("Contact Status", max_length=20)

    def __str__(self):
        return self.status

class Contact(models.Model):
    first_name = models.CharField("First name", max_length=255, null = False)
    last_name = models.CharField("Last name", max_length=255, null = False)
    account = models.ForeignKey(Account, related_name='lead_account_contacts', on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null = False)
    address = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    createdBy = models.ForeignKey(User, related_name='contact_created_by', on_delete=models.CASCADE)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class ActivityStatus(models.Model):
    status = models.CharField("Activity Status", max_length=20)

    def __str__(self):
        return self.status

class Activity(models.Model):
    description = models.TextField(blank=True, null=False)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=False)

    def __str__(self):
        return self.description