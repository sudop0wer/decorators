# Decorators Login System
A Python script for managing a simple user authentication system using classes and decorators.

## Overview

The decorators script is a Python implementation of a login management system, using classes and decorators to enforce user authentication on specific functions. Here’s a breakdown of its main components:
1. User Class: This class defines user-related functionality, such as login and logout. It handles user authentication by storing the login state and provides methods to log in and out.
2. Decorator (@requires_authentication): This decorator is applied to specific functions to restrict access only to logged-in users. When a decorated function is called, the decorator checks if the user is logged in; if not, it returns an error or prompts login, enforcing security.
3. Public and Restricted Functions: The script defines functions to demonstrate the decorator's functionality:
  - Public Functions: Accessible by anyone, regardless of authentication status.
  - Restricted Functions: Decorated with @requires_authentication, these functions require a user to be logged in. Examples include posting messages or viewing profiles.

### Example Workflow
- A user logs in using the User class’s login method.
- They can access restricted functions while logged in.
- On logout, access to restricted functions is blocked until they log in again.

This design pattern demonstrates effective use of decorators for authentication, providing a simple yet flexible login management example.

## Installation
1. Clone the repository.
2. Run decorator.py using Python 3.

## Usage
- Add user credentials in the script.
- Use login and logout functions to authenticate.
- Access restricted functions with authentication.

## Contributions
Contributions are welcome. Please fork the repository and submit a pull request with improvements.
