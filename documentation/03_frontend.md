# The Glorious Frontend

The frontend is simple. 

ReactJS is used with a chatbot package to create a simple chat button and then the entire chat window.

Admittedly, the chatbot package has barebones documentation and can be a bit hard to understand. But it does the job
and is easy to use once it makes sense.

We tried to follow ReactJS guidelines but none of us knew React before starting this, and so some of the code may seem like
it has been **hackathoned** together. This may sometimes be the case. We did plan to refactor but did not have enough time.

### Features implemented

The form that appears at the end of the chat is powered by TypeForm. It is easy to integrate, as it is just an embedded iFrame object.
It saves all results in a Google Sheet. The client had asked us to explore Microsoft Forms to integrate better with University
technologies but we did not have time to do that.

The option to send an email to the client was done by sending a request to the Django server using Axios and giving it the necessary parameters.
Django then sends the email accordingly using SendGrid. This feature was admittedly rushed as it was right when we had coursework
due and everything was hell. So please try to refactor this if you can to make it better.

The text-to-speech option was a nightmare to implement. The chatbot package does have an option to enable this but actually doing it
seems impossible. The documentation is very sparse and did not show how to enable and disable this feature programatically.
In the end, we had to use the library ResponsiveVoice. The script for it is placed in ```client/public/index.html```. A script was also
placed in that same file called ```window.ttsOn``` and is a boolean. Basically, we use a global for controlling the sound and then manually
call the ResponsiveVoice API if this boolean is true. It is a bit of a hacky solution, and we are a bit proud of it considering
all the time we spent trying to do it the *proper* way. One may argue that this is the *proper* way.


