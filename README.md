# User Management Application

User Management Application built using [FastAPI](https://fastapi.tiangolo.com/) and [Sqlalchemy](https://www.sqlalchemy.org/)(postgres).

## Setup
### Using Bash
```bash
if command -v curl >/dev/null 2>&1; then
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/shreyas-acharya/UserApplication/HEAD/install.sh)"
else
    bash -c "$(wget -O- https://raw.githubusercontent.com/shreyas-acharya/UserApplication/HEAD/install.sh)"
fi
```
### Using Docker
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
