django-rest-user-profiles
-------------------------

A small app which creates a user profile with a display name and avatar when a user is registerred.
The app lets the user upload an avatar.


Quick start
-----------

1. Add "userprofile" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rest_user_profiles',
    ]

2. Include the userprofile URLconf in your project urls.py like this::

	from django.conf.urls import include

    url(r'^users/', include('rest_user_profiles.urls')),

3. To create the rest-user-profiles models run:

	python manage.py makemigrations rest_user_profiles
	python manage.py migrate


