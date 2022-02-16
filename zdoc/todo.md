Private route. Prevent login route when user already login

• Building a follow system
#The relationship between users is a many-to-many relationship: a user can follow multiple users and they, in turn, can be followed by multiple users

#Create an intermediary model to build relationships between users. There are two reasons for using an intermediary model:

-   You are using the User model provided by Django and you want to avoid altering it
-   You want to store the time when the relationship was created and probably describe the nature of the relationship

• Creating many-to-many relationships with an intermediary model

• Creating an activity stream application

-   Build a generic activity stream _application_ that every user can see recent interactions of the users they follow.

*   Adding generic relations to your models with Contenttype objects.

• Adding generic relations to models
• Optimizing QuerySets for related objects
• Using signals for denormalizing counts
• Storing item views in Redis

Prevent user from following themselves
