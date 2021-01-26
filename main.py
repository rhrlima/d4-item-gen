from tests import test_data, test_generator
from flask_app import app


# running basic tests
test_data.run_tests()
test_generator.run_tests()

# running flask server
# access at localhost:5000
app.app.run()