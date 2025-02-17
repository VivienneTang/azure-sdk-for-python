# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from datetime import timedelta
from devtools_testutils import recorded_by_proxy

from callautomation_test_case import CallAutomationRecordedTestCase

class TestCallAutomationClientAutomatedLiveTest(CallAutomationRecordedTestCase):

    @recorded_by_proxy
    def test_create_VOIP_call_and_answer_then_hangup(self):
        # try to establish the call
        caller = self.identity_client.create_user()
        target = self.identity_client.create_user()
        unique_id, call_connection, _ = self.establish_callconnection_voip(caller, target)

        # check returned events
        connected_event = self.check_for_event('CallConnected', call_connection._call_connection_id, timedelta(seconds=15))
        participant_updated_event = self.check_for_event('ParticipantsUpdated', call_connection._call_connection_id, timedelta(seconds=15))

        if connected_event is None:
            raise ValueError("Caller CallConnected event is None")
        if participant_updated_event is None:
            raise ValueError("Caller ParticipantsUpdated event is None")

        self.terminate_call(unique_id)
        return

