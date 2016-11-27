def custom_attributes(user, service):
    return {'givenName': user.first_name, 'email': user.email}