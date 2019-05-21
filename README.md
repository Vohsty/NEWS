# MC17 NEWS

## Description
#### This is a web application that displays a list of various news sources from which a user can access news. A user can search for news articles of their liking as well and view them on the source website. The app makes use of the [News API](https://newsapi.org/).
#### By **STEVE KIMANTHI**
The user can:
* See various news sources
* View articles from a news source they like
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source
## Setup/Installation Requirements
### Prerequisites
* python3.6
* pip
* Virtual environment(virtualenv)

### Cloning and running
* Clone the application using git clone(this copies the app onto your device). In terminal:

          $ git clone https://github.com/Vohsty/NEWS.git
          $ cd ijnews

* Creating the virtual environment

          $ python3.6 -m venv --without-pip virtual
          $ source virtual/bin/env
          $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

          $ python3.6 -m pip install Flask
          $ python3.6 -m pip install Flask-Bootstrap
          $ python3.6 -m pip install Flask-Script
* Setting up the API Key

To be able to gather article info from the News API you will need an API Key.

* Visit https://newsapi.org/ and register for an API key.
* In the root directory of the project folder create a file: start.sh
* Insert the following info into it:

          export NEWS_API_KEY='<Your-Api-Key>'
          python3.6 manage.py server

* Insert the API Key you received from News Api where <Your-Api-Key> is.

* Run the application:

          $ chmod a+x start.sh
          $ ./start.sh
### Testing the Application
* To run the tests for the class files:

          $ python3.6 manage.py test

## Technologies Used
* Python 3.6
* Flask
## Behaviour driven development/ Specifications

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| Display news sources | On page load | List of various news sources is displayed per category |
| Display articles from a news source | Click a news source | Redirected to a page with a list of articles from the source |
| Display the preview of an article | On page load | Each article displays an image, title, author, summary and link to source site |
| Read an entire article | Click an article | Redirected to the news source's site to read the entire article |

## Support and contact details
For any questions, troubleshooting or contributions,  find me on:
* Mobile: +254710998712
* Email: vohsty@gmail.com
### License
MIT License
Copyright (c) {2019} **Steve Kimanthi**
