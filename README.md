# Railway Management System

The Railway Management System is a Python application that integrates with MySQL using `mysql.connector` to facilitate various railway operations. It provides functionalities for ticket booking, cancellation, account management, and real-time updates to the database.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- **Ticket Booking:** Users can book train tickets.
- **Ticket Cancellation:** Allows users to cancel their booked tickets.
- **Delete Account:** Option to delete user accounts from the system.
- **Sign Up:** New users can register their accounts.
- **Account Details:** View and update user profile information.
- **Sign In:** Authentication for accessing user-specific functionalities.
- **Ticket Checking:** Check the status of booked tickets.

## Installation

### Prerequisites

- Python 3.x
- MySQL Server

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/arcui03/Railway-Management-System.git

2. Install dependencies:
   ```bash
   pip install mysql-connector-python
3. Set up MySQL database:
   - Create a database named `railway_reservation`.
   - Import the SQL schema to set up the necessary tables.
4. Configure MySQL connection:
   - Update your python file with your MySQL database credentials:
     ```python
db_config = {
    'host': 'localhost',
    'database': 'railway_reservation',
    'user': 'your_username',
    'password': 'your_password',
}

## Usage

1. Run the application:
```bash
python main.py
```

2. Follow the on-screen instructions to navigate through various functionalities.

## Contributing
Contributions are welcome! If you have any ideas or improvements, please feel free to fork the repository and submit a pull request.

Thank You
Archit Tiwari

