# Assignment microservices
API in Flask continerizzate con Mysql e MongoDb 

## List of microservices 
>1. [Books microservice](./TEST_FINALE/books):
>expose CRUD opereration, use flask framework and mysql database
>1. [Customer microservice](./TEST_FINALE/customer):
>expose CRUD opereration, use flask framework and mysql database
>1. [Borrowing microservice](./TEST_FINALE/borrowing):
>expose CRUD opereration, use flask framework and mongoDB database


Develop 4 microservices as depicted in this diagram:

![](./img/diagram.png)

Microservices can be developed in any any techology , but they must comply with following constraints:

- Use HTTP/REST for synchronous communication
- Use at least two different database technology (RDBMS and NoSQL).
- Use a message broker (Kafka, Active MQ, Rabbit MQ) for asynchronous communications (ie: calling the Notification service)

Evaluation criteria:

- Microservices         (0 to 5 points)
- Design patterns       (0 to 5 points)
- Testing               (0 to 5 points)
- Logging and tracing   (0 to 5 points)
- CI/CD                 (0 to 5 points)
- Docker and Kubernetes (0 to 5 points)

Impostazione servizio loggin
![](./img/1.png)

Struttura del collegamneto fra i microservizi 
![](./img/my_diagram.drawio.png)
