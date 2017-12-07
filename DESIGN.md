# Eventr

### Design intent
The idea for Eventr was intended to make it easier to find as well as navigate things going on on campus. One thing I've found here on campus my freshman year is that having too much going on can be as much of an issue as having too little going on. It is often difficult to narrow down between the choices I do have, and because of the surplus of events, I often find myself missing out on events I want to go to. For lack of time (or effort), I find myself ignoring the posters seen throughout the yard and proctor boards. I created Eventr with the intent to ease the process of navigating all of these events. I've worked on other projects with similar intention. For instance for HCS, I created an addition to HarvardNow that texts the user the next 10 events posted on the FAO website.

### Media Choice
I originally intended for this app to be implemented as an iOS application, as I figured it would be much more useful to have a mobile version of the application. Unfortunately, a few difficulties stopped me from completing the iOS app to my satisfaction. While I did accomplish the goals I had originally set out for myself with the iOS application (creating a frontend app that can take pictures or select pictures from a service), going beyond this was very difficult. I had no experience with Swift prior, so every step in development was a battle. To even get the development environment functioning took an unreasonable amount of time. So while I was able to get a client-app functioning and taking pictures, the app did not interface properly with the OCR api, which was the heart of the app, and had relatively little function. With the time I had left after the Hackathon, I felt that I could create an app with greater functionality using flask, and I did so with the web implementation of Eventr. With that said, I hope to continue to develop the iOS app, and hopefully get it to the level of the web app.

## The Good Stuff

### Flask App
This program is implemented as a flask app. The versatility of python libraries and the ease of making API calls in python really made it ideal. For this project, I used both an optical character recognition API, as well as a library that finds potential dates within strings. Both of these would have to have been re-coined in other languages/frameworks, which would have increased an already limited development time

## Logic
### Main Page
The main page of the website is a simple landing page that explains how the app is used. Like all of the other pages on the app, it has a nav-bar on the top which is derived from layout.html

### Scan Page
This is the page where the majority of the work on the app is done. On this page is a form that selects a file from the users computer, the user also inputs a title. Various helper functions verify that a title exists, and the the file attempted to be inputted is in an image format and not harmful. If the file is valid, a POST request is made to an optical character recognition API in order to get the text of the image. This text is then returned to the app, where the datefinder library is used to find any potential dates. If a valid date is returned, then the event is added to the sql database, and the user is rerouted to the events page. If the OCR api either does not work or there are no valid matches, then the user is rerouted to manually enter the event.

### Manual Page
This is a page where a user can manually enter an event. Once again, the user can upload the event poster, and input a title. This time however, the user also inputs a date. If all of these inputs are valid, it is added to the database.

### Events Page
This page renders all of the events in the database in a table, with entries for the event title and the date. All of the events in the page are click-able, and lead to a page that renders the event poster. The dynamic rendering of the table and the dynamic reference assignments to all event entries were done using Jinja. The event pages are a link in the form ```/event/<id>```

### Event Page
This page is used to render the image of any given event. It does so by using the event id provided in the link, and retrieving that file from the static folder in the server

### About Page
This page credits the app's creator and documents upcoming features.

## Python files
### application.py
Application.py handles the entirety of the routing done for this application. The logic behind the routing for each page is explained in the corresponding entry above.

### helpers.py
Helpers.py contains the various database helper functions that are used to make queries and inserts into tables in the database much more readable. It also contains a function to ensure that only image filetypes are allowed to be submitted to the web-site (for security purposes)
