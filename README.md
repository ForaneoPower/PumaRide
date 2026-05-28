# PumaRide

![Python Logo](https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.enesmorelia.unam.mx%2Fla-enes-unidad-morelia-informa%2F&ved=0CBYQjRxqFwoTCKin-aTu3JQDFQAAAAAdAAAAABAG&opi=89978449)

* Universidad Nacional Autónoma de México (UNAM)
* Escuela nacional de Estudios Superiores Unidad Morelia (ENES Morelia)

## Team 4: Collaborators:

* Technology Engineer: Adrián Lara adrianlara.jpg@gmail.com
* Testing Engineer: Emiliano Ramírez emi4play777@gmail.com
* Project Manager: Grecia Arias greciariaass@gmail.com

## Licence: 

GNU General Public License v3.0

## Description:

An open source project made by and for college students of ENES Morelia in 
mind that aims 
to give them a platform where they can request free rides depending on 
where they are and where they want to go within the community members of 
UNAM Morelia
 -development-


## Methodology:

For developing this project we used differents requiremets:

* This project relies completely on the openrouteservice API. It provides the necessary tools to calculate the most
effective routes in the map. (API link: https://openrouteservice.org)
* Leaflet is used for the interactive map UI.
* We are using FastAPI for the structure itself, and we manage data requests using HTTP.
* We are using Django for the creation of the creation of the web application
* It will have registered the data of only an user and a driver.

## Implementation:
* Bsckend: Python, Django
* 
* Frontend: HTML, CSS, JavaScript

## Installation and execution for development:

### Instalation:

1. Clone the repository: git clone https://github.com/ForaneoPower/PumaRide?tab=GPL-3.0-1-ov-file
2. Create and activate the virtual environment: python -m venv venv

 source venv/bin/activate (for linux)

3. Install required packages: pip install -r requirements.txt

### Execution:

1. To start the local development server using **Uvicorn**, run the following command:

uvicorn main:app --reload


## Testing:



## Results:

A functional web application was developed that asks for the initial point of the route and retunrns the most effective route with the objective of being used by the driver and the passenger
