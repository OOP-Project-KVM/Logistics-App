# Logistics Application

## Overview

The Logistics Application is designed to help manage and track the logistics of delivering packages via predefined routes. The system supports user registration, logging in as employees, managing routes, assigning trucks, and assigning packages to these routes. It calculates the expected arrival time of packages based on the departure time, distance, and average speed of the trucks.

## Features

- **User Registration and Login:**
  - Employees can register and log in to access the system.
  - Roles include `Manager` and `Worker`.

- **Route Management:**
  - Create routes with specified locations and departure times.
  - Assign trucks to routes.
  - Search for routes between specific locations.

- **Package Management:**
  - Create packages with details such as start and end locations, weight, and customer contact information.
  - Assign packages to routes, with the system automatically calculating and setting the expected arrival time.
  - View details of unassigned packages.
  - View detailed information about specific packages.

- **Truck Management:**
  - Assign trucks to routes based on availability and capacity.
  - View details of available trucks and their assignments.

- **Calculation of Expected Arrival Time:**
  - The system calculates the expected arrival time for each package based on the departure time and distance to the destination.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/logistics-application.git
   cd logistics-application
