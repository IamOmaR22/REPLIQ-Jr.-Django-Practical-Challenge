# Enterprise Device Management API
---
This Django application provides an API for managing enterprise devices, employees, companies, device logs, and subscriptions. It allows companies to efficiently manage their devices and subscriptions for their employees.

## Features

- **Company Management:** CRUD operations for managing companies.
- **Employee Management:** CRUD operations for managing employees within companies.
- **Device Management:** CRUD operations for managing devices owned by companies.
- **Device Logs:** Track the history of device check-in and check-out actions.
- **Subscription Management:** Manage subscriptions for enterprise clients.

## API Endpoints

### Companies
- **List Companies:**
  - `GET /companies/`

- **Retrieve Company:**
  - `GET /companies/<company_id>/`

- **Create Company:**
  - `POST /companies/`

- **Update Company:**
  - `PUT /companies/<company_id>/`
  - `PATCH /companies/<company_id>/`

- **Delete Company:**
  - `DELETE /companies/<company_id>/`

### Employees
- **List Employees:**
  - `GET /employees/`

- **Retrieve Employee:**
  - `GET /employees/<employee_id>/`

- **Create Employee:**
  - `POST /employees/`

- **Update Employee:**
  - `PUT /employees/<employee_id>/`
  - `PATCH /employees/<employee_id>/`

- **Delete Employee:**
  - `DELETE /employees/<employee_id>/`

### Devices
- **List Devices:**
  - `GET /devices/`

- **Retrieve Device:**
  - `GET /devices/<device_id>/`

- **Create Device:**
  - `POST /devices/`

- **Update Device:**
  - `PUT /devices/<device_id>/`
  - `PATCH /devices/<device_id>/`

- **Delete Device:**
  - `DELETE /devices/<device_id>/`

- **Check Out Device:**
  - `POST /devices/<device_id>/check_out/`

- **Check In Device:**
  - `POST /devices/<device_id>/check_in/`

### Device Logs
- **List Device Logs:**
  - `GET /devicelogs/`

- **Retrieve Device Log:**
  - `GET /devicelogs/<devicelog_id>/`

- **Create Device Log:**
  - `POST /devicelogs/`

- **Update Device Log:**
  - `PUT /devicelogs/<devicelog_id>/`
  - `PATCH /devicelogs/<devicelog_id>/`

- **Delete Device Log:**
  - `DELETE /devicelogs/<devicelog_id>/`

### Subscriptions
- **List Subscriptions:**
  - `GET /subscriptions/`

- **Retrieve Subscription:**
  - `GET /subscriptions/<subscription_id>/`

- **Create Subscription:**
  - `POST /subscriptions/`

- **Update Subscription:**
  - `PUT /subscriptions/<subscription_id>/`
  - `PATCH /subscriptions/<subscription_id>/`

- **Delete Subscription:**
  - `DELETE /subscriptions/<subscription_id>/`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IamOmaR22/REPLIQ-Jr.-Django-Practical-Challenge.git
   ```

2. Create a virtual environment:
   ```bash
   cd REPLIQ-Jr.-Django-Practical-Challenge
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the API at `http://localhost:8000/`

## Testing

To run tests, use the following command:
```bash
python manage.py test
```

## Documentation

API documentation can be accessed at `/swagger/` or `/redoc/` when the server is running.

## Built With

- Django - Web framework
- Django REST framework - Toolkit for building Web APIs
- SQLite - Database
- Other dependencies listed in `requirements.txt`

## Future Improvements

- Implement user authentication and authorization.
- Integrate with a payment gateway for subscription management.
- Enhance documentation with more detailed examples.
- Implement frontend application for easier management.

## Contributors

- Md. Omar Faruk - iamomar022@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
