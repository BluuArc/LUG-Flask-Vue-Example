# LUG-Flask-Vue-Example

## Disclaimer

The code shown here is an example of an implementation of using a Vue frontend and Flask backend. This does not necessarily represent the final implementation. The main purpose of this repository is to be used as a reference for this kind of infrastructure.

## What's This?

This is an implementation of a basic web app using a Vue frontend and Flask backend.

## Minimum Requirements

* Python 3.6 (v2.x not tested)
  * need [Flask](http://flask.pocoo.org/docs/1.0/) and [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
* Node 8.9.4 (other versions untested)
* npm (only tested with 6.4.0)

## How to Run/Serve
* If the web app isn't built yet, navigate to the `sample-client` folder and run `npm run build`
* Follow the instructions [here](http://flask.pocoo.org/docs/1.0/quickstart/) to run the `server.py` file.
  * basic idea is to create a `FLASK_APP` console variable with `server.py` as its value, then running `flask run`

## How to Develop

* navigate to `sample-client`
* run `npm install` to install dependencies locally
* run `npm run serve` to start the development server
  * when data is changed in the `sample-client` folder, the page should auto-reload when the dev server is active
* You can run the Flask server concurrently to help test integration of API with frontend

## Project Structure
* `sample-client` - Vue.js project for the front end portion of the web application
  * `src` - contains source code of web application
  * `dist`- contains public distributed version of web application
* `server.py`
  * `/` - serves `index.html` of compiled web application
  * `/static/` - serves static assets needed by web application
  * `/api/posts` - returns an array of some mock post data

## Things to Consider for Final Implementation
* Site Design
  * This version is a very rough mockup of the first page of the [current LUG site](http://lug.cs.uic.edu/) using [Bulma](https://bulma.io/) as the main CSS framework with [Less](http://lesscss.org/) as the CSS preprocessor
* Backend Design
  * I suggest using `/api/` for all API endpoints to separate RESTful calls from the frontend assets, but this may change
* Testing
  * This version has no testing (frontend or backend)
