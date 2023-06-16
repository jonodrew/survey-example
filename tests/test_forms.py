from django.test import TestCase, SimpleTestCase

from pulse_survey.survey import forms


# TODO - these tests should be changed if we add validation for Cabinet Office emails

class FeedbackFormTest(TestCase):
    def test_incorrect_email(self):
        form = forms.FeedbackForm({"email": "not an email", "content": ""})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue("Enter a valid email address" in str(email_errors))

    def test_good_email_with_bad_domain(self):
        form = forms.FeedbackForm({"email": "test@example.com", "content": "some feedback"})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue("Please enter a Cabinet Office email address" in str(email_errors))

    def test_good_email(self):
        cases = (
            {"case": "No 10", "address": "PM@No10.gov.uk"},
            {"case": "GDS", "address": "CEO@digital.cabinet-office.gov.uk"},
        )
        for test_case in cases:
            with self.subTest(test_case['case']):
                form = forms.FeedbackForm({"email": test_case['address'], "content": "some feedback"})
                form.is_valid()
                no_email_errors = "email" not in form.errors
                self.assertTrue(no_email_errors)


class CabinetOfficeValidationTest(SimpleTestCase):
    def test_is_cabinet_office_email(self):
        cases = (
            {"case": "No 10", "address": "PM@No10.gov.uk"},
            {"case": "GDS", "address": "CEO@digital.cabinet-office.gov.uk"},
        )
        for test_case in cases:
            with self.subTest(test_case['case']):
                result = forms.is_cabinet_office_email(test_case['address'])
                self.assertTrue(result)


