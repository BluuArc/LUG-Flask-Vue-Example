# LUG-Flask-Vue-Example

## Disclaimer

The code shown here is an example of an implementation of using a Vue frontend and Flask backend. This does not necessarily represent the final implementation. The main purpose of this repository is to be used as a reference for this kind of infrastructure.

## What's This?

This is an implementation of a basic web app using a Vue frontend and Flask backend.

## How to Run/Serve
* If the web app isn't built yet, navigate to the `sample-client` folder and run `npm run build`
* Follow the instructions [here](http://flask.pocoo.org/docs/1.0/quickstart/) to run the `server.py` file.

## How to Develop

* navigate to `sample-client`
* run `npm run serve`
  * when data is changed in the `sample-client` folder, the page should auto-reload
* You can run the server concurrently to help test integration of API with frontend

## Things to Consider for Final Implementation
* Site Design
  * This version is a very rough mockup of the first page of the [current LUG site](http://lug.cs.uic.edu/) using Bulma as the main CSS framework
* Backend Design
  * I suggest using `/api/` for all API endpoints to separate RESTful calls from the frontend assets, but this may change
* Testing
  * This version has no testing (frontend or backend)
