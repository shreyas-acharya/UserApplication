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
3. Build the docker images, containers and volumes
```
docker compose build
```
4. Start the application
```
docker compose up
```
5. Stop and remove the containers
```
docker compose down
```

## Endpoints
| Endpoint | Type | Input Format | Description | 
| ---------| ---- | ------------ | ----------- |
| /addUser | POST | `{ username: str, password: str, fullname: str, email: str, age: int }` | Add new user |
| /getUsers| GET  | - | Returns a list of all users |
| /getLogs | GET | - | Returns login and logout logs |
| /login | POST | `{ username: str,password: str }` | Login |

### Once logged in the following endpoints can be accessed
| Endpoint | Type | Input Format | Description |
| -------- | ---- | ------------ | ----------- |
| /getUser | GET | - | Display the details of the user |
| /updateUser | PATCH | `{ password: str, fullname: str, email: str, age: int }` **Note:** All the attributes are optional | Update user information |
| /deleteUser | DELETE | - | Delete user |
| /logout | POST | - | Logout |
