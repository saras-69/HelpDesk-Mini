# 🎫 HelpDesk Mini - Modern Ticketing System

A comprehensive Django-based helpdesk ticketing system with SLA tracking, modern glassmorphism UI, and REST API.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-3.0+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Compatible-blue.svg)

## ✨ Features

### 🎯 Core Functionality
- **Ticket Management**: Complete CRUD operations with UUID-based IDs
- **SLA Tracking**: Automatic deadline calculation based on priority
- **User Roles**: User, Agent, and Admin role-based access control
- **Comment System**: Threaded comments with parent-child relationships
- **Timeline Tracking**: Comprehensive audit log for all ticket changes
- **Search & Filter**: Full-text search with status and priority filtering

### 🔒 Security & Performance
- **Optimistic Locking**: Version control for concurrent updates
- **CSRF Protection**: Django security best practices
- **UUID Primary Keys**: Enhanced security for ticket IDs
- **Proper Authentication**: Session-based authentication with role management

### 🎨 Modern UI/UX
- **Glassmorphism Design**: Beautiful blur effects and transparency
- **Animated Background**: Smooth gradient animations
- **Responsive Layout**: Mobile-first responsive design
- **Tailwind CSS**: Modern utility-first CSS framework
- **Interactive Elements**: Smooth transitions and hover effects

### 🔌 API Features
- **RESTful API**: Complete REST endpoints for all operations
- **Pagination**: Efficient data loading with page-based pagination
- **Filtering**: API-level filtering by status, priority, and assignment
- **Versioning**: Built-in optimistic locking for PATCH operations

## 📋 SLA Tracking

| Priority | Response Time | Badge Color |
|----------|---------------|-------------|
| Critical | 4 hours       | 🔴 Red      |
| High     | 24 hours      | 🟡 Yellow   |
| Medium   | 72 hours      | 🔵 Blue     |
| Low      | 168 hours     | ⚪ Gray     |

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL (or SQLite for development)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saras-69/SKILLION.git
   cd SKILLION
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework psycopg2-binary python-decouple
   ```

4. **Configure environment**
   ```bash
   # Create .env file with your database credentials
   echo "DATABASE_URL=your_postgresql_connection_string" > .env
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   Open http://127.0.0.1:8000 in your browser

## 📁 Project Structure

```
HelpDesk/
├── HelpDesk/                 # Project settings
│   ├── settings.py           # Django configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── accounts/                 # User management
│   ├── models.py            # Custom User model
│   ├── views.py             # Authentication views
│   └── urls.py              # Auth URL patterns
├── tickets/                  # Core ticketing system
│   ├── models.py            # Ticket, Comment, Timeline models
│   ├── views.py             # Ticket CRUD views
│   ├── api_views.py         # REST API endpoints
│   ├── serializers.py       # DRF serializers
│   └── templatetags/        # Custom template tags
├── templates/               # HTML templates
│   ├── base.html           # Base template with glassmorphism
│   ├── tickets/            # Ticket-specific templates
│   └── registration/       # Auth templates
└── static/                 # Static files and Tailwind config
```

## 🔗 API Endpoints

### Tickets
- `GET /api/tickets/` - List all tickets (paginated)
- `POST /api/tickets/` - Create new ticket
- `GET /api/tickets/{id}/` - Get ticket details
- `PATCH /api/tickets/{id}/` - Update ticket (with optimistic locking)
- `DELETE /api/tickets/{id}/` - Delete ticket

### Comments
- `POST /api/tickets/{id}/comments/` - Add comment to ticket
- `GET /api/tickets/{id}/comments/` - List ticket comments

### Filtering & Search
- `GET /api/tickets/?search=query` - Search tickets
- `GET /api/tickets/?status=open` - Filter by status
- `GET /api/tickets/?priority=high` - Filter by priority
- `GET /api/tickets/?assigned_to=user_id` - Filter by assignee

## 🎨 UI Components

### Glassmorphism Effects
- **Glass Cards**: Semi-transparent containers with backdrop blur
- **Glass Navigation**: Blurred header with transparency
- **Glass Inputs**: Form elements with blur effects
- **Animated Background**: Gradient animation with CSS keyframes

### Status Badges
- **Open**: Blue badge for new tickets
- **In Progress**: Yellow badge for active tickets
- **Resolved**: Green badge for completed tickets
- **Closed**: Gray badge for finalized tickets

## 🔧 Configuration

### Database Settings
Configure your database in `settings.py` or use environment variables:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': '5432',
    }
}
```

### Tailwind CSS
The project uses Tailwind CSS via CDN with custom glassmorphism effects. No build process required.

## 🧪 Testing

Run the system tests:
```bash
python test_ticket.py
```

This will verify:
- User creation and authentication
- Ticket creation with SLA calculation
- Comment system functionality
- Status updates and timeline tracking
- Database operations

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False` in settings.py
2. Configure proper `ALLOWED_HOSTS`
3. Set up static file serving
4. Use environment variables for sensitive data
5. Configure HTTPS and security headers

### Recommended Stack
- **Frontend**: Current Django templates with Tailwind CSS
- **Backend**: Django + PostgreSQL
- **Deployment**: Heroku, DigitalOcean, or AWS
- **Database**: PostgreSQL (Neon for cloud)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support, email support@helpdesk-mini.com or create an issue in this repository.

## 🙏 Acknowledgments

- **Django**: Web framework
- **Tailwind CSS**: Utility-first CSS framework
- **PostgreSQL**: Robust database system
- **Django REST Framework**: API development
- **Neon**: Cloud PostgreSQL platform

---

**Built with ❤️ using Django and modern web technologies**