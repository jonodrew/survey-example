import string

from django.test import TestCase

from pulse_survey.survey import models


class FeedbackModelTest(TestCase):
    def test_feedback_saved(self):
        feedback = models.Feedback(email="Test@Example.Com", content="Some feedback")
        feedback.save()
        self.assertEqual(feedback.content, "Some feedback")

    def test_email_saved_in_lower_case(self):
        email = "MixTuRe.of.CAPiTals@cabinetoffice.gov.uk"
        feedback = models.Feedback(email=email, content="Not important")
        feedback.save()
        self.assertTrue(set(feedback.email).isdisjoint(set(string.ascii_uppercase)), "No uppercase in email")
