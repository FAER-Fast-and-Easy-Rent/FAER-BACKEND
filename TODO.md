# FAER : A Rental System -> TODO

- [x] Setup app with restframework

  - Install necessary dependencies
  - Created django-project named core
  - Created a app named api
  - Added urls for index in core
  - Setup for restframework along with urls done
  - Included api urls
  - Tested home index url with some messgae and status-code
  - Added github action workflow along with flake and coverage support
  - Added few settings for simplejwt

- [x] Setting up Accounts

  - Added Manager and model for the custom user along with forms
  - Added functionality for the user in admin view
  - Added tests for testing create_user and creste_superuser
  - Added register user view
  - Added retrieve user view
  - Added user serializer
  - Registered URL for user creation and retrieval
  - Tested all routes for accounts with the postman
  - Added all tests for accounts and verified

- [x] Setting up Models(Room and Media) and kafka

  - Added Room and Media model along with its serializer and views
  - Created compose file for Kafka
  - Created producer and consumer for the app
  - Refactored models and logic for the rooms
  - Removed some unused models
  - Added event-based task under rooms
  - Consumed create_room task and added logic for room creation along with the transaction
  - Added logic for the image file to be stored into temp and it's deletion
  - Changed the response status for creation of the room i.e 201
  - Added validators for a unique title
  - Added tests for room creation ,retrieval and validation

- [x] Add feature for the vehicle
  - Added model for Vehicle
  - Added serializer for vehicle
  - Added viewset for the vehicle
  - Updated serializer fields and viewsets
  - Added consumer for the Vehicle
  - Added task/function for vehicle creation
  - Added Tests for the vehicle creation ,retrieval and validation
  - Refactored some of the components
  - Added Models fields description to todo.md
