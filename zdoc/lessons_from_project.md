Creating Login view

Creating many-to-many relationships
Customizing behavior for forms
Using jQuery with Django
Building an app with jQury
Generating image thumbnails and integrating them with jQuery
Creating custom decorators for views
Building AJAX pagination

I learned the benefit of `related_name `

One-to-many Relationship:
Instance of B:
One user can have multiple images.
An image can only be to one user

many-to-many Relationship:
One user can like multiple images.
An image can be liked by multiple users

When you need to repeat a queryset in your template, use the {% with %} template tag to avoid additional database queries. Ensure there is no space between the equal sign.

Features such as like should be performed in an asynchronous manner. This was the page is not reloaded.

In this chapter, you created models with many-to-many relationships and learned
how to customize the behavior of forms. You used jQuery with Django to build
a JavaScript bookmarklet to share images from other websites into your site. This
chapter has also covered the creation of image thumbnails using the easy-thumbnails
library. Finally, you implemented AJAX views with jQuery and added AJAX
pagination to the image list view.
In the next chapter, you will learn how to build a follow system and an activity
stream. You will work with generic relations, signals, and denormalization. You
will also learn how to use Redis with Django.

you will learn how to build a follow system and create a user activity
stream. You will also discover how Django signals work and integrate Redis's fast
I/O storage into your project to store item views.

=========

## MANY-TO-MANY RELATIONSHIP WITH AN INTERMEDIARY MODEL.

Sometimes you may need to create an intermediary model you want to store additional information for the relationship, for example, the date the relationship was created, or the field that describes the nature of the relationship.

## Using the contenttypes framework

Django includes a contenttypes framework located at django.contrib.contenttypes. This application can track all models installed in your project and provides a generic interface to interact with your models.
