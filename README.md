# webcred
A Python API that calculates surface, content and off-page features and writes to a locally stored MongoDB database.

Surface Features:
  Top Level Domain, Count of Inlinks, Outlinks, Broken Links, Advertisements, Page Load Time, Internationalization, Responsiveness, Last Modified Date and Time, Contact Info, Image to text ratio
  
Content Features:
  Spelling Errors, Grammar Errors, Subjectivity, Polarity, POS Tagging
  
Off-Page Features:
  Backlinks Count
  
  
A Chrome Extension that stores the value of the current URL of a page and returns the value in the browser.

The goal is to call the API from the extension and calculate the credibility of the webpage from the features, and display it in the extension.
