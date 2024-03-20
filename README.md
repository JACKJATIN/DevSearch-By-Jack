# Devsearch - Platform for Developers

Devsearch is a web application designed for developers to showcase their projects, interact with other users via messaging, and participate in project ranking through upvotes and downvotes. The platform also allows users to display their skills and expertise.

## Features

- **Project Showcase**: Developers can showcase their projects with detailed descriptions, screenshots, and links to repositories or live demos.
- **Messaging System**: Users can communicate with each other privately through an inbox messaging system.
- **Voting System**: Projects can be upvoted or downvoted by users, allowing for community-driven ranking.
- **Skills Display**: Users can display their skills and expertise on their profiles.
- **Django Backend**: Backend functionality is implemented using Django, providing a robust and scalable architecture.
- **Static File Serving with Whitenoise**: Static files are served efficiently using Whitenoise.
- **Amazon S3 Bucket**: Media storage for user-uploaded files, such as project images, is handled by Amazon S3 for scalability and reliability.
- **Three Applications**: The project is structured into three Django applications: `users`, `projects`, and the main `devsearch` app.
- **Environment Variables**: Sensible configuration and sensitive data are managed using environment variables.
- **Deployment on Render**: The application is deployed on Render for easy scalability and continuous integration and deployment.

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript
- Django templates
- UI Kits (e.g., Bootstrap, Materialize CSS)

### Backend
- Django
- Django forms
- Django REST Framework (for building RESTful APIs)

### Deployment
- Render (for deployment)
- Amazon S3 (for media storage)

## Setup and Configuration

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
