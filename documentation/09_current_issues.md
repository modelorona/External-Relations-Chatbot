## Current Issues

These are issues we identified but were not able to fix in time.

## Current issues
### Refactor the database to have proper relations and be more flexible
The database was modelled after the initial short courses csv file that we were given. We needed to work fast as there was other stuff to do, and so did not take the time
to properly figure out relations and make multiple tables in the database. If the relations were modelled, this could result in less complicated and faster queries, and would
follow proper SQL database modelling guidelines.
### Refactor React code to make it follow proper React practices
Currently our React code is not structured correctly according to React coding conventions.
### Phase out firebase
Firebase was great for a demo but not so much in the long run. The one function that it uses to communicate with DialogFlow could be integrated into Django as a view url
and then this would completely eliminate the use of Firebase.
### Figure out better way to integrate text-to-speech
The current implementation of the text-to-speech feature is quite 'hacky'. There is a window variable in the index.html file that is updated
every time the text-to-speech is turned on and off. We add this as we could not find a way to keep a global variable for this using Node
### Look into Microsoft Forms instead of TypeForm
The clients expressed interest in us finding a Microsoft service to deal with the feedback form as they already use a lot of Microsoft services.
Time did not allow for us to fully investigate this.
### Find some way to encourage the user to take the feedback form
The clients expressed interest in finding a way to encourage user to actually leave feedback as right now the feedback form is only prompted when
a user says 'bye' to the chatbot. This could probably be improved by triggering the feedback form with a timeout when the user has be inactive for
a while or a pop up of some sort on the main page.
### In the admin page, allow the client to mass upload a csv file of courses
There is currently no way in the admin page to allow the clients to upload a csv file of courses. New courses have to be added one by one, and this is tedious.
### After adding a new course, Django should generate synonyms for all of these courses, and add these synonyms as well as the original entity to DialogFlow.
This would allow for a relatively low maintenance way to update the agent with new courses and their synonyms whenever the clients decide to add new courses. This issue goes hand in hand with
the one above.
