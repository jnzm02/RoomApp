from django.contrib.auth.decorators import user_passes_test


def check_user(user):
    return not user.is_authenticated


user_logout_required = user_passes_test(check_user, '/', None)


def auth_user_should_not_access(viewfunc):
    return user_logout_required(viewfunc)

# def check_creator(user, room):
#     if room.creator == user.username:
#         return True
#
# def creator_only(viewfunc):
#     return check_creator(viewfunc);
