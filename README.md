# User Management Application

User Management Application built using [FastAPI](https://fastapi.tiangolo.com/) and [Sqlalchemy](https://www.sqlalchemy.org/)(postgres).

## Setup
### Prerequisites:
- [Docker](https://docs.docker.com/get-docker/)
### Steps:
1. Clone the repository
```
git clone https://github.com/shreyas-acharya/UserApplication.git
```
2. Create a .env file in the same level as the docker-compose.yml file.   
The .env file format is as follows :
```
USERNAME=<postgres_username>
PASSWORD=<postgres_password>
DATABASE=<database_name>
```
4. Start the application
```
docker compose -f ./docker-compose.yml up // Non persistent storage (suitable for testing)
docker compose -f ./docker-compose.yml -f ./docker-compose-production.yml up // Persistent storage (suitable for production environment)
```
5. Stop and remove the containers
```
docker compose -f ./docker-compose.yml down
(or)
docker compose -f ./docker-compose.yml -f ./docker-compose-production.yml down
```

## Endpoints
| Endpoint | Type | Input Format | Description | 
| ---------| ---- | ------------ | ----------- |
| /addUser | POST | `{ username: str, password: str, fullname: str, email: str, age: int }` | Add a new user |
| /getUsers| GET  | - | Returns a list of all users |
| /getLogs | GET | - | Returns login and logout logs |
| /login | POST | `{ username: str,password: str }` | Login |

### Once logged in the following endpoints can be accessed
| Endpoint | Type | Input Format | Description |
| -------- | ---- | ------------ | ----------- |
| /getDetails| GET | - | Display the details of the user |
| /updateUser | PATCH | `{ password: str, fullname: str, email: str, age: int }`<br>**Note:** All the attributes are optional | Update user details |
| /deleteUser | DELETE | - | Delete user |
| /logout | POST | - | Logout |
