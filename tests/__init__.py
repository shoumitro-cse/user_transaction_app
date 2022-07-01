"""
    To run all test case:
    python manage.py test tests
"""

from accounts.tests import TokenTests, UsersTests, UserProfileTests
from transactions.tests import TransactionsTests

