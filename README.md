# ADA2021

Team Bombardierii ADA 
Members: Darius Milea(CEO), Miron Florin (CTO), Raul Chincea(COO)

Project name: Delivero

Project short description: Universal delivery service.

Project description: 

  There are two different types of clients for the service, one is the android app used to track and interact with the courier, the web app is used by the service user, which wants something to be delivered to them. 
  Servers are used to handle different services that together make the whole app work the way it does. Website will be delivered using a webserver.
  The services delivered by servers are:
    - User service, such as login/register/session control
    - Order service, such as taking/managing orders for clients and couriers
    - Courier Tracking service, such as tracking location of each courier

Use case: 
  
   Joe is hungry, he wants to eat from his favorite place, Shaorma City. He lives far away from that place and he doesn't own a car so he wants the food to be delivered to him. He uses the website to order food from his favorite place. After he places an order that ordered is sent to the corresponding area server which appoints a courier to deliver the food. The courier gets a notification and information about the order and the addresses. The courier delivers the food to Joe and he pays for it. 
   
Technologies used: 
  - Web frontend REACT
  - Android for phone app
  - Django and postgresql for API
  - Message broker: RabbitMQ
  - Tracking service: Google Maps API