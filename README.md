
# Equipo 4


# PumaRide
An open source project made by and for college students of ENES Morelia in 
mind that aims 
to give them a platform where they can request free rides depending on 
where they are and where they want to go within the community members of 
UNAM Morelia
 -development-

## Collaborators:

* Technology Engineer: Adrián Lara Álvarez
* Testing Engineer: Emiliano Ramírez
* Project Manager: Grecia Leilani Arias Avalos

## Usage of app.py in routing-service in a development enviroment
To use this test script and obtain information from the openrouteservice API, Yo
you first need to install the necessary dependencies (FastAPI, uvicorn, python-dotenv, openrouteservice)

After that, you need access to your own API key which you will use to communicate
with the openrouteservice server. You can get it for free by logging in their site
and opening the API playground. Using your API key, you will modify your .env file
and the script should work properly.

In your terminal and in the directory pumaride/routing-service, run:

uvicorn app:app --reload

Then in your browser use the link that shows up on the terminal followed by /docs
to open the Swagger UI.

In this interface, you can try out the API using the correct format. Entering two
coordinates in [lon, lat]. It should return a .JSON file with the names of both
the start point and the end point, followed by the distance in km and the 
estimated duration of the trip in minutes. You might want to use these for ease of use:

start: -101.230103,19.647981
end: -101.217813,19.679336

If you wish to enter your own coordinates, go to the [following link](https://maps.openrouteservice.org/#/)
and search for both the start and end point you want.
