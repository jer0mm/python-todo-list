from utils.data_reader import DataReader
from utils.logger import get_logger
from tests.test_login import LoginTest

# initialize logger
logger = get_logger()

# create objects
data_reader = DataReader()
login_test = LoginTest()

# read test data
users = data_reader.read_user_data('test_data/users.json')

passed = 0
failed = 0

# execute tests
for user in users:
    try:
        result = login_test.login(user['username'], user['password'])

        if result == user['expected']:
            logger.info(f"Test PASSED for user {user['username']}")
            passed += 1
        else:
            logger.error(f"Test FAILED for user {user['username']}")
            failed += 1

    except Exception as e:
        logger.error(f"Exception occurred: {e}")
        failed += 1

# summary
print("Test Execution Summary")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
