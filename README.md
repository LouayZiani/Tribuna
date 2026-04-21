# Tribuna: KPL Football Ticket Booking Platform

> A full-stack web application for browsing and booking football tickets for the Kazakhstan Premier League.  
> Built with **Angular** (frontend) + **Django REST Framework** (backend).

---

## Group Members

| Name | GitHub |
|------|--------|
| Louay Ziani | [@LouayZiani](https://github.com/LouayZiani) |
| Nursultan A. | [@nursayag17](https://github.com/nursayag17) |
| A. Zhaparov | [@AZhaparov07](https://github.com/AZhaparov07) |

> **Practice Lesson:** Wednesday 15-17  

---

## Project Description

**Tribuna** simulates a real-world football ticket booking platform for the Kazakhstan Premier League (KPL). Users can register, log in, browse upcoming matches, view stadium seat layouts, and book tickets for VIP or Regular sections. The platform tracks seat availability in real time and links each booking to the authenticated user.

---

## Features

- Browse upcoming KPL matches
- Stadium seat map with VIP and Regular sections
- Real-time seat availability tracking
- Ticket booking linked to authenticated user
- JWT-based login / logout
- Error handling with user-facing messages

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Angular 21, TypeScript, FormsModule, HttpClient |
| Backend | Django, Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Database | SQLite or PostgreSQL (we're still undecided)|
| CORS | django-cors-headers |

---

## Requirements Coverage

### Frontend (Angular)

| # | Requirement | Implementation |
|---|-------------|----------------|
| 1 | Interfaces & services for API | `Match`, `Seat`, `Ticket`, `User` interfaces; `ApiService`, `AuthService` |
| 2 | ≥ 4 click events triggering API requests | Book seat, cancel ticket, login, logout, load matches |
| 3 | ≥ 4 form controls with `[(ngModel)]` | Login form, registration form, booking form, seat filter |
| 4 | Basic CSS styling | Component-level CSS for all pages |
| 5 | Routing with ≥ 3 named routes | `/home`, `/matches`, `/booking/:id`, `/login` |
| 6 | `@for` and `@if` (Angular 17+) | Match list loop, seat availability conditional render |
| 7 | JWT auth: interceptor, login, logout | `AuthInterceptor`, `LoginComponent`, `AuthService.logout()` |
| 8 | ≥ 1 Angular Service with HttpClient | `ApiService` handles all HTTP calls |
| 9 | API error handling | Error messages displayed in UI on failed requests |

### Backend (Django + DRF)

| # | Requirement | Implementation |
|---|-------------|----------------|
| 1 | ≥ 4 models | `User` (extended), `Match`, `Seat`, `Ticket` |
| 2 | Custom model manager (optional) | `AvailableSeatManager` on `Seat` |
| 3 | ≥ 2 ForeignKey relationships | `Ticket → Match`, `Ticket → User`, `Seat → Match` |
| 4a | ≥ 2 `serializers.Serializer` | `LoginSerializer`, `SeatAvailabilitySerializer` |
| 4b | ≥ 2 `serializers.ModelSerializer` | `MatchSerializer`, `TicketSerializer` |
| 5a | ≥ 2 Function-Based Views | `login_view`, `logout_view` (with DRF decorators) |
| 5b | ≥ 2 Class-Based Views (`APIView`) | `MatchListView`, `TicketCreateView` |
| 6 | Token-based auth (login + logout) | JWT via `SimpleJWT`, custom endpoints |
| 7 | Full CRUD for ≥ 1 model | Full CRUD on `Ticket` |
| 8 | Link objects to `request.user` | `Ticket.user = request.user` on creation |
| 9 | CORS configured | `django-cors-headers` allowing `http://localhost:4200` |
| 10 | Postman collection | See `/postman/tribuna.postman_collection.json` |

---

## Project Structure

```
tribuna/
├── frontend/               # Angular project
│   └── src/app/
│       ├── components/     # Match list, seat map, booking, login
│       ├── services/       # ApiService, AuthService
│       ├── interceptors/   # AuthInterceptor (JWT)
│       └── interfaces/     # Match, Seat, Ticket, User
├── backend/                # Django project
│   ├── matches/            # Match model, views, serializers
│   ├── tickets/            # Ticket model, CRUD views
│   ├── seats/              # Seat model, availability logic
│   └── accounts/           # Auth endpoints (login/logout)
└── postman/
    └── tribuna.postman_collection.json
```

---

## Getting Started

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
ng serve
```

App runs at `http://localhost:4200`, API at `http://localhost:8000`.

---

## Postman Collection

All API endpoints with example requests and responses are documented in:  
`/postman/tribuna.postman_collection.json`
