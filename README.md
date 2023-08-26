# Corporate Asset Tracking System

The Corporate Asset Tracking System is a web application built using Django that enables companies to efficiently manage their corporate assets, such as phones, tablets, laptops, and other devices, which are handed out to employees. The application provides a streamlined way for companies to track the distribution, condition, and history of assets, ensuring effective asset management across different teams and departments.

## Features

- **Multi-Company Support**: The application is designed to accommodate multiple companies, allowing each company to manage their own set of employees and devices.

- **Employee and Device Management**: The system enables companies to add employees and devices to their profile. Employees can be associated with a specific company, and devices can be categorized by their name and condition.

- **Device Delegation**: Companies can delegate devices to employees for a specified period. The application enforces a check to ensure that devices are not delegated if they are already issued to an employee.

- **Device Log**: The system maintains a log of each device's checkout and return. It records the employee, condition, and timestamps of both actions.

- **API Support**: The application offers a RESTful API for managing companies, employees, devices, and device logs. This API allows developers to integrate asset tracking functionality into other systems.

## Getting Started

1. **Installation**: Clone this repository and Install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

2. **Database Setup**: Run database migrations using:

    ```bash
    python manage.py migrate
    ```

3. **Create Superuser**: Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

4. **Run Development Server**: Start the development server:

    ```bash
    python manage.py runserver
    ```

5. **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` to add companies, employees, devices, and manage device logs.

6. **API Endpoints**: Use the provided API endpoints to manage assets programmatically. Refer to the API documentation for more details.


## API Documentation

The API provides the following endpoints:

- `/companies/`: List and create companies.
- `/employees/`: List and create employees.
- `/assets_list/`: List and create assets. assets can also be delegated to employees.
- `/assets_list/<int:id>`: Get, update and delete specific asset with id 
- `/assets_logs/`: List and create asset logs. asset logs record checkout and return actions.
- `/assets_logs/<int:id>`:
  - **PATCH**: Update details of a asset log.
  - **DELETE**: Delete a asset log.
- `/assets_logs/company/<str:company_name>/`: Filter asset logs by company name.
- `assets_logs/employee/<int:employee_id>/`: Filter asset logs by employee ID.

- `/assets_logs/company/<str:company_name>/`: Filter device logs by company name.

## Contributors

- Pavel-Khan17
- pavelkhan.dev@gmail.com
