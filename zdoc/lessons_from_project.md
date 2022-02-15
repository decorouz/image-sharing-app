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
