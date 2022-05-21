import json
import unittest
from src.application import create_app
from urllib.parse import urlencode

class TestReport(unittest.TestCase):

    def test_create_report(self):
        app = create_app().test_client()
        response = app.get("/policy.docx?data=%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22address%22%3A%20%2205452%20Bass%20Path%5CnSanchezport%2C%20MI%2026978%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22birthdate%22%3A%20%2224-01-1954%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22blood_group%22%3A%20%22AB-%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22company%22%3A%20%22Watkins%2C%20Evans%20and%20Meyer%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22job_title%22%3A%20%22Professor%20Emeritus%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22last_name%22%3A%20%22Lambert%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22name%22%3A%20%22Michael%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22policy%22%3A%20%22V57166%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22sex%22%3A%20%22M%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22ssn%22%3A%20%22409-45-2021%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D")
        self.assertEqual(response.status_code, 200)