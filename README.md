# shapesproject
https://shapesproject.herokuapp.com/

Description, Django Rest Framework (DRF)

Problem
  Create RESTful API what will allow:
    - User registration
    - Login
    - User can CRUD shapes of type:
      - Triangle
      - Rectangle
      - Square
      - Diamond
    - User can request for shapes:
      - Area
      - Perimeter
      
Rules of shape:
  Square: All sides are equal
  Rectangle: 1 side must be longer than the other
  Diamond: All sides are equal, but 2xSide must be greater than height.
  Triangle: Sum of 2 sides of a triangle must be greater than the 3rd side.
  Design
  
This project consists of 3 main apps:
  1) Accounts – For handling user registration and logins and returning API endpoints.
  2) API - For handling CRUD functions of the 4 shapes using API.
  3) Shapes_app – For the web application that communicates with the first 2 apps.
 
Accounts
  - 1 customuser model
  - Uses DRF inbuilt Basic and Session authentication.
  - Created a customuser model that inherits AbstractUser. (email as username)
  - For simplicity, no email activation needed. The account is automatically set to is_active on successful
    registration.
  - CBV for getting user details, registration and login.
 
API
  - 1 model for storing shapes data with user foreign key.
  - CBVs to get, create, update and delete shapes assigned to user.
    - Different properties are collected for different shapes.
    - Includes conditions that flags error in shapes creation/updates.
    	eg: Sum of 2 sides of a triangle must be greater than the 3rd side.
    - Error should lead to an API endpoint with error message but for simplicity, I stored the shape
      nonetheless with error remarks.
    - Conducts area and perimeter calculations based on collected properties for valid shapes.
    - Invalid shapes will be stored with error remarks and 0 value for area and perimeter.
    
Shapes_app
  - HTML templates, CSS and Javascript files to communicate with API endpoints.
  - NOTE: for the purpose of displaying some API endpoints, the user will be directed to the API endpoint upon login and registration.
  - Login required to use the CRUD operation.
  - Frontend not mobile-friendly, please view the project on larger devices.
  - Shapes page displaying CRUD operations automatically requests all shapes and properties for the user.
  - Select the shape you want to update and use the same shape form above to make changes.
 
Database
  - SQLite
