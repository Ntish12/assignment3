"""
Employee Management System Module

This module provides various functionalities for managing employee data.
"""

# Define the list of modules to be imported when the package is imported
# This list specifies the modules that will be imported when using "from package import *"
# In this case, only the main_menu module is exposed to the user
__all__ = ['menu']

# Import the main_menu module from the src.menu submodule
# This import statement allows the main_menu function to be accessed directly from the package
# Users can use "from package import main_menu" to access the main_menu function
from .src.menu import menu
