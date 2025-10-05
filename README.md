# 🎫 HelpDesk Mini - Modern Ticketing System

> A comprehensive Django-based helpdesk ticketing system with SLA tracking, modern glassmorphism UI, and REST API.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-3.0+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Compatible-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## 📖 Table of Contents

- [Features](#-features)
- [SLA Tracking](#-sla-tracking)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [UI Components](#-ui-components)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [Support](#-support)

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 **Core Functionality**
- ✅ **Ticket Management** - Complete CRUD with UUID-based IDs
- ⏰ **SLA Tracking** - Auto deadline calculation by priority
- 👥 **User Roles** - User, Agent, Admin access control
- 💬 **Comment System** - Threaded parent-child comments
- 📝 **Timeline Tracking** - Comprehensive audit logs
- 🔍 **Search & Filter** - Full-text search with filtering

</td>
<td width="50%">

### 🔒 **Security & Performance**
- 🔐 **Optimistic Locking** - Version control for updates
- 🛡️ **CSRF Protection** - Django security best practices
- 🆔 **UUID Primary Keys** - Enhanced security for tickets
- 🔑 **Authentication** - Session-based role management

</td>
</tr>
<tr>
<td width="50%">

### 🎨 **Modern UI/UX**
- ✨ **Glassmorphism Design** - Blur effects & transparency
- 🌈 **Animated Background** - Smooth gradient animations
- 📱 **Responsive Layout** - Mobile-first design
- 🎯 **Tailwind CSS** - Modern utility-first framework
- 🖱️ **Interactive Elements** - Smooth transitions

</td>
<td width="50%">

### 🔌 **API Features**
- 🌐 **RESTful API** - Complete REST endpoints
- 📄 **Pagination** - Efficient data loading
- 🎛️ **Filtering** - API-level filtering options
- 🔄 **Versioning** - Optimistic locking for PATCH

</td>
</tr>
</table>

## 📋 SLA Tracking

<div align="center">

| Priority | ⏱️ Response Time | 🏷️ Badge Color | 📊 Status |
|----------|------------------|----------------|-----------|
| **Critical** | 4 hours | 🔴 Red | Urgent |
| **High** | 24 hours | 🟡 Yellow | Important |
| **Medium** | 72 hours | 🔵 Blue | Standard |
| **Low** | 168 hours | ⚪ Gray | Routine |

</div>

---

## 🚀 Quick Start

### 📋 Prerequisites

<table>
<tr>
<td>🐍 <strong>Python</strong></td>
<td>3.11+</td>
</tr>
<tr>
<td>🗄️ <strong>Database</strong></td>
<td>PostgreSQL (or SQLite for development)</td>
</tr>
<tr>
<td>📦 <strong>Git</strong></td>
<td>Latest version</td>
</tr>
</table>

### ⚡ Installation

<details>
<summary><strong>🔽 Click to expand installation steps</strong></summary>

#### **Step 1: Clone the repository**
```bash
git clone https://github.com/saras-69/HelpDesk-Mini.git
cd HelpDesk-Mini
```

#### **Step 2: Set up virtual environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### **Step 3: Install dependencies**
```bash
pip install django djangorestframework psycopg2-binary python-decouple
```

#### **Step 4: Configure environment**
```bash
# Create .env file with your database credentials
echo "DATABASE_URL=your_postgresql_connection_string" > .env
```

#### **Step 5: Set up database**
```bash
python manage.py makemigrations
python manage.py migrate
```

#### **Step 6: Create admin user**
```bash
python manage.py createsuperuser
```

#### **Step 7: Start the server**
```bash
python manage.py runserver
```

#### **Step 8: Access the application**
🌐 Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser

</details>

---

## 📁 Project Structure

<details>
<summary><strong>🔽 Click to view project structure</strong></summary>

```
HelpDesk/
├── 🏗️ HelpDesk/                 # Project settings & configuration
│   ├── settings.py               # 🔧 Django configuration
│   ├── urls.py                   # 🛣️ URL routing
│   └── wsgi.py                   # 🌐 WSGI configuration
├── 👤 accounts/                  # User management system
│   ├── models.py                 # 📊 Custom User model
│   ├── views.py                  # 🎭 Authentication views
│   └── urls.py                   # 🔗 Auth URL patterns
├── 🎫 tickets/                   # Core ticketing system
│   ├── models.py                 # 🗃️ Ticket, Comment, Timeline models
│   ├── views.py                  # 🎭 Ticket CRUD views
│   ├── api_views.py              # 🔌 REST API endpoints
│   ├── serializers.py            # 📋 DRF serializers
│   └── templatetags/             # 🏷️ Custom template tags
├── 🎨 templates/                 # HTML templates
│   ├── base.html                 # 🖼️ Base template with glassmorphism
│   ├── tickets/                  # 🎫 Ticket-specific templates
│   └── registration/             # 🔐 Authentication templates
└── 📦 static/                    # Static files & Tailwind config
    └── src/
        └── input.css             # 🎨 Custom CSS styles
```

</details>

---

## 🔗 API Documentation

<details>
<summary><strong>🔽 Click to view API endpoints</strong></summary>

### 🎫 Ticket Endpoints

| Method | Endpoint | Description | Features |
|--------|----------|-------------|----------|
| `GET` | `/api/tickets/` | 📋 List all tickets | ✅ Pagination |
| `POST` | `/api/tickets/` | ➕ Create new ticket | ✅ Validation |
| `GET` | `/api/tickets/{id}/` | 🔍 Get ticket details | ✅ Full data |
| `PATCH` | `/api/tickets/{id}/` | ✏️ Update ticket | ✅ Optimistic locking |
| `DELETE` | `/api/tickets/{id}/` | 🗑️ Delete ticket | ✅ Soft delete |

### 💬 Comment Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/tickets/{id}/comments/` | ➕ Add comment to ticket |
| `GET` | `/api/tickets/{id}/comments/` | 📋 List ticket comments |

### 🔍 Filtering & Search

| Parameter | Example | Description |
|-----------|---------|-------------|
| `search` | `?search=bug` | 🔍 Search in title/description |
| `status` | `?status=open` | 📊 Filter by status |
| `priority` | `?priority=high` | ⚡ Filter by priority |
| `assigned_to` | `?assigned_to=123` | 👤 Filter by assignee |

### 📝 Example API Usage

```bash
# Get all tickets with pagination
curl -X GET "http://localhost:8000/api/tickets/?page=1"

# Search for tickets
curl -X GET "http://localhost:8000/api/tickets/?search=login%20issue"

# Create a new ticket
curl -X POST "http://localhost:8000/api/tickets/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Login Issue", "description": "Cannot login", "priority": "high"}'
```

</details>

---

## 🎨 UI Components

<details>
<summary><strong>🔽 Click to view UI details</strong></summary>

### ✨ Glassmorphism Effects

<table>
<tr>
<td width="50%">

#### 🃏 **Glass Cards**
- Semi-transparent containers
- Backdrop blur effects
- Subtle border highlights
- Shadow depth

</td>
<td width="50%">

#### 🧭 **Glass Navigation**
- Blurred header background
- Transparent navigation bar
- Smooth scroll effects
- Responsive design

</td>
</tr>
<tr>
<td width="50%">

#### 📝 **Glass Inputs**
- Form elements with blur
- Focus state animations
- Floating labels
- Validation styling

</td>
<td width="50%">

#### 🌈 **Animated Background**
- CSS gradient keyframes
- Smooth color transitions
- Performance optimized
- Mobile-friendly

</td>
</tr>
</table>

### 🏷️ Status Badge System

| Status | Color | Icon | Description |
|--------|-------|------|-------------|
| **Open** | 🔵 Blue | 📋 | New tickets awaiting response |
| **In Progress** | 🟡 Yellow | ⚡ | Actively being worked on |
| **Resolved** | 🟢 Green | ✅ | Issue has been fixed |
| **Closed** | ⚪ Gray | 🔒 | Completed and archived |

</details>

---

## 🔧 Configuration

<details>
<summary><strong>🔽 Click to view configuration options</strong></summary>

### 🗄️ Database Settings

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

### 🎨 Tailwind CSS Setup

The project uses **Tailwind CSS via CDN** with custom glassmorphism effects:
- ✅ No build process required
- ✅ Custom utility classes included
- ✅ Responsive design ready
- ✅ Dark mode compatible

### 🔐 Environment Variables

Create a `.env` file in your project root:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/helpdesk
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

</details>

---

## 🧪 Testing

<details>
<summary><strong>🔽 Click to view testing information</strong></summary>

### 🚀 Run System Tests

Execute the comprehensive test suite:

```bash
python test_ticket.py
```

### ✅ Test Coverage

The test suite verifies:

| Component | Test Coverage |
|-----------|---------------|
| 👤 **User Management** | Authentication & role assignment |
| 🎫 **Ticket Creation** | CRUD operations & SLA calculation |
| 💬 **Comment System** | Threading & parent-child relationships |
| 📊 **Status Updates** | Workflow transitions & timeline |
| 🗄️ **Database Operations** | Data integrity & performance |

### 📋 Test Categories

- **Unit Tests**: Individual component testing
- **Integration Tests**: API endpoint validation
- **Functional Tests**: User workflow testing
- **Performance Tests**: Load and response time testing

</details>

---

## 🚀 Deployment

<details>
<summary><strong>🔽 Click to view deployment guide</strong></summary>

### 🔧 Production Settings Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Set up static file serving
- [ ] Use environment variables for sensitive data
- [ ] Configure HTTPS and security headers
- [ ] Set up database connection pooling
- [ ] Configure logging and monitoring

### 🌐 Recommended Technology Stack

<table>
<tr>
<td><strong>🎨 Frontend</strong></td>
<td>Django Templates + Tailwind CSS</td>
</tr>
<tr>
<td><strong>🔧 Backend</strong></td>
<td>Django + PostgreSQL</td>
</tr>
<tr>
<td><strong>☁️ Deployment</strong></td>
<td>Heroku, DigitalOcean, AWS, or Railway</td>
</tr>
<tr>
<td><strong>🗄️ Database</strong></td>
<td>PostgreSQL (Neon for cloud)</td>
</tr>
<tr>
<td><strong>📦 Static Files</strong></td>
<td>WhiteNoise or AWS S3</td>
</tr>
</table>

### 🐳 Docker Deployment (Optional)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

</details>

---

## 🤝 Contributing

<details>
<summary><strong>🔽 Click to view contribution guidelines</strong></summary>

We welcome contributions! Here's how you can help:

### 🚀 Getting Started

1. **🍴 Fork the repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR-USERNAME/HelpDesk-Mini.git
   ```

2. **🌿 Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **💻 Make your changes**
   - Follow Python/Django best practices
   - Add tests for new functionality
   - Update documentation as needed

4. **✅ Test your changes**
   ```bash
   python test_ticket.py
   python manage.py test
   ```

5. **📝 Commit your changes**
   ```bash
   git commit -m 'Add: amazing new feature'
   ```

6. **📤 Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **🔄 Open a Pull Request**
   - Provide a clear description
   - Reference any related issues
   - Include screenshots if UI changes

### � Contribution Guidelines

- **Code Style**: Follow PEP 8 for Python code
- **Commits**: Use conventional commit messages
- **Testing**: Add tests for new features
- **Documentation**: Update README if needed

### 🐛 Bug Reports

Found a bug? Please include:
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Screenshots (if applicable)

</details>

---

## 📞 Support

<div align="center">

### 🆘 Need Help?

| Type | Contact |
|------|---------|
| 📧 **Email** | support@helpdesk-mini.com |
| 🐛 **Bug Reports** | [Create an Issue](https://github.com/saras-69/HelpDesk-Mini/issues) |
| 💡 **Feature Requests** | [Discussion Board](https://github.com/saras-69/HelpDesk-Mini/discussions) |
| 📚 **Documentation** | [Wiki](https://github.com/saras-69/HelpDesk-Mini/wiki) |

</div>

---

## 🙏 Acknowledgments

<div align="center">

### 🛠️ Built With

| Technology | Purpose | Version |
|------------|---------|---------|
| 🐍 **[Django](https://djangoproject.com/)** | Web Framework | 5.2.7 |
| 🎨 **[Tailwind CSS](https://tailwindcss.com/)** | Styling Framework | 3.0+ |
| 🗄️ **[PostgreSQL](https://postgresql.org/)** | Database System | Latest |
| 🔌 **[Django REST Framework](https://django-rest-framework.org/)** | API Development | Latest |
| ☁️ **[Neon](https://neon.tech/)** | Cloud PostgreSQL | - |

### 💝 Special Thanks

- Django community for the amazing framework
- Tailwind CSS team for the utility-first approach
- PostgreSQL team for the robust database system
- All contributors and users of this project

</div>

---

<div align="center">

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
<h3>🎯 <strong>Built with ❤️ using Django and modern web technologies</strong></h3>

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![Made with Django](https://img.shields.io/badge/Made%20with-Django-green.svg)
![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)

<p><strong>⭐ Star this repository if you found it helpful!</strong></p>

</div>

</div>#   H e l p D e s k - M i n i 
 
 