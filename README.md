# Webcred

Webcred is a customizable browser plug-in that can evaluate the credibility of a web page using various surface, content and off-page features.

Surface Features:
  Top Level Domain, Count of Inlinks, Outlinks, Broken Links, Advertisements, Page Load Time, Internationalization, Responsiveness, Last Modified Date and Time, 
  Contact Info, Image to text ratio
  
Content Features:
  Spelling Errors, Grammar Errors, Subjectivity, Polarity, POS Tagging
  
Off-Page Features:
  Backlinks Count
  
The project consists of a login page, an extension and a database. Users are directed to a login page where they enter their credentials using either Google, 
GitHub or Twitter, then they select the weightage assigned to various features. This information is stored in a database and is used to calculate the 
credibility score of the website being visited.

The login page is built using flask and associated flask libraries such as flask-dance, flask-wtf and flask-wtforms. The login page uses OAuth clients from the
respective mediums and makes use of blueprints. The blueprints contain information such as the API key and secret key, the redirect URL and the authorized URLs.
These URLs must be specified in the API clients as well in order to ensure the app works as expected. Separate blueprints are registered with the Flask App to
ensure that all three mediums can be used to authorize users. 

The preferences page contains the selection for various genres and feature categories along with fields to enter the user's preferences. 
In the event that the user does not wish to enter this data, the default weightages are used for each feature.

All the information is stored in a MongoDB database which contains the tables Fact, Feature, Genre and User. 
Fact stores the website URL, scores of individual features, surface score, content score, off-page score, aggregate score and timestamp. Feature contains the user
ID, genre, and the weightages of each feature. The genre table stores the genre ID, name, user ID and timestamp. The user table stores User ID, username, 
medium used to log in, and the timestamp. PyMongo is used to create an interface between the python app and the database. 

The extension is the main part of the app that will be used by the end-users. It contains a front-end created using HTML, CSS and JavaScript. It displays the 
URL, the genre and the credibility score. 

The Django framework is used to connect the browser extension to the rest of the app which calculates the credibility score and genre. [PENDING]
