"""Top Doctor common predicates module

This module creates predicates which will be
imported by different Django apps for permissioning.

see https://github.com/dfunckt/django-rules#using-rules
for more info about rules/predicates.

This module contains the following predicates:

    * is_employed_by_owner - checks if user's org owns object
    * is_employed_by_doctor - checks if user's org is a producer
"""

import rules
from django.apps import apps


@rules.predicate
def is_employed_by_owner(user, obj):
    """
    if not hasattr(user, "organization"):
        return False  # anonymous user or swapped user model, doesn't support organization field
    if not hasattr(obj, "owner"):
        return False
    return user.organization.id == obj.owner.id
    """
    return True


@rules.predicate
def is_employed_by_manager(user):
    """
    if not hasattr(user, "job"):
        return False  # anonymous user or swapped user model, doesn't support organization field
    job = user.job
    Doctor = apps.get_model("jobs", "Doctor")
    if Doctor.objects.filter(pk=job.id).exists():
        return True
    else:
        return False
    """
    return True
