import rules

from eminoglu.rules import is_employed_by_manager, is_employed_by_owner


@rules.predicate
def can_add_sinif(user):
    if not hasattr(user, "is_active"):
        return False  # anonymous user or swapped user model, doesn't support is_active field
    return (
        user.is_active
        & rules.is_authenticated(user)
        & (
            rules.is_superuser(user)
            | (is_employed_by_owner(user, user) & is_employed_by_manager(user))
        )
    )
