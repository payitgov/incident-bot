from bot.googlemeet.meeting import GoogleMeet
import os
import config
import pytest
from google.auth.exceptions import RefreshError

class TestIncidentMeeting:
    def test_incident_meeting(self):

        if "googlehangout" in config.active.integrations:
            try:
                hangout = GoogleMeet()
                hangout.create_meeting()
                hangout.delete_meeting()

                assert hangout.meeting_info["hangout_link"]
            except RefreshError as e:
                pytest.skip(f"Skipping test due to invalid Google credentials: {e}")
            except Exception as e:
                # Re-raise other exceptions as they indicate actual test failures
                raise
