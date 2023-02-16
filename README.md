# User Management Application

User Management Application built using (FastAPI)[https://fastapi.tiangolo.com/] and (Sqlalchemy)[https://www.sqlalchemy.org/].

## Setup
### Prerequisites:
- (Docker)[https://docs.docker.com/get-docker/]


## Endpoints
| Endpoint | Type | Input Format | Description | 
| ---------| ---- | ------------ | ----------- |
| /addUser | POST | `{ username: str, password: str, fullname: str, email: str, age: int }` | Add new user |
| /getUsers| GET  | None | Returns a list of all users |
| /deleteUser/{username} | DELETE | None | Delete user |
| /getLogs | GET | None | Returns the user's login and logout logs |
| /login | POST | `{ username: str,password: str }` | Login |


Once logged in the following endpoints can be accessed
| /getUser | GET | None | Display the details of the user |
| /updateUser | PATCH | `{ password: str, fullname: str, email: str, age: int }` **Note:** All the attributes are optional | Update user information |
| /logout | POST | None | Logout |
