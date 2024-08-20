# Logistics-App

Welcome to our Logistics console application!

## Project Description

The application will be used by employees of a large Australian company aiming to expand its activities to the freight industry. The app will be used to manage the delivery process of packages between hubs in major Australian cities.

## Available functionalities

### The application supports the following functionalities:

* #### Adding customers to the *system*

* #### Creating and managing delivery packages

* #### Creating and managing delivery routes

* #### View information about routes, packages and trucks

## Avalilable commands
### _You need to login as either _**employee**_, _**supervisor**_ or _**manager**_ in order to use the system!_

### The application supports the following commands:

* _**addcustomer**_ -  you will be asked to provide first and last name, as well as email and phone number

* _**createpackage**_ - the package will be associated with a customer by email, you will also be asked for information about the package - weight and start and end location; you will be able to assign the new package to a suitable route that already exists, or you could create a new route for it
* _**viewpackage**_ - searches for a package by ID
* _**viewallpackages**_ - you need to be logged in as SUPERVISOR, provides information about all packages
* _**viewunassignedpackages**_ - you need to be logged in as SUPERVISOR, provides information about all packages that are not yet assigned to a delivery truck

* _**createdeliveryroute**_ - you can provide all the expected route stops, and you will need to set a departure date (in the following format: 'Dec 25 2024 15:45h')
* _**viewdeliveryroute**_ - provides information about a route by its ID
* _**viewalldeliveryroutes**_ - you will need to be logged in as MANAGER, returns information about all delivery routes
* _**viewroutesinprogress**_ - only a MANAGER has access to this command, returns information about active delivery routes

* _**assigntrucktoroute**_ - this is what triggers the delivery process, you will need to provide a route ID, the system returns a list of suitable trucks and you will be able to pick one to assign

* _**listalltrucks**_ - lists all trucks with status _available_

* _**timeforward**_ - simulates the state of the system 5 days after the currect date and time

* _**help**_ - at any point you can type in _help_ to display information about all supported commands


### _You need to logout before exiting the system!_