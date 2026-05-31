# PumaRide
---

<p align="center">
  <img src="https://github.com/user-attachments/assets/519cdbc4-09da-4dfd-a304-fee05cd55fea" width="360" />
  <img src="https://github.com/user-attachments/assets/5fcb5c81-0422-4742-a38a-9db59e0f54f9" width="360" />
</p>

---

## Institution

* **Universidad Nacional Autónoma de México (UNAM)**
* **Escuela Nacional de Estudios Superiores Unidad Morelia (ENES Morelia)**

## About the Project

**PumaRide** is an open-source project created for the Cloud Computing course, apart of the Data Science major.
The project aims to provide a community-based ride-sharing platform where students can request and offer free rides within the college community. The goal is to facilitate collaborative transportation for college students.

![Testing](images/Testing)

## Team 4 - Collaborators


* **Technology Engineer** - Adrián Lara [adrianlara.jpg@gmail.com](mailto:adrianlara.jpg@gmail.com)
* **Testing Engineer** - Emiliano Ramírez [emi4play777@gmail.com](mailto:emi4play777@gmail.com)   
* **Project Manager** Grecia Arias [greciariaass@gmail.com](mailto:greciariaass@gmail.com)

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0): **https://www.gnu.org/licenses/gpl-3.0.en.html 

## Tech Stack

### Backend

* Python
* Django
* FastAPI
* Uvicorn
* nginx
* OpenRouteService API
* AWS EC2

### Frontend

* HTML
* CSS
* JavaScript
* Leaflet

## Methodology

The development of this project relies on the following technologies and tools:

* **OpenRouteService API** is used to calculate efficient routes between two coordinates.
  Website: https://openrouteservice.org

* **Leaflet** is used to build the interactive map interface.
  Website: https://leafletjs.com/

* **FastAPI** handles API development and HTTP request management.
  Website: https://fastapi.tiangolo.com/

* **Django** is used for the web application structure and backend management.
  Website: https://www.djangoproject.com/

* **AWS EC2** was used alongside **nginx** during deployment.
  Website: https://aws.amazon.com/

## Installation and Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ForaneoPower/PumaRide.git
cd PumaRide
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Development Server

In the main directory, start the local **Django** server running:

```bash
python manage.py runserver
```

Inside the routing-service directory, start the local development server using **Uvicorn**:

```bash
uvicorn app:app --port 8001
```
Navigate to the [following page](http://127.0.0.1:8000/) in your preferred browser.

## Deployment

In order to skip the installation process and test the service directly, an EC2 instance was used with an elastic IP that automatically starts the app on your browser. You can use it in the [following link](http://100.49.84.140/)

## Results:

A functional web application was developed that asks for the initial point of the route by clicking the map and retunrns the most effective route with the objective of being used by the driver and the passenger of the ride.
