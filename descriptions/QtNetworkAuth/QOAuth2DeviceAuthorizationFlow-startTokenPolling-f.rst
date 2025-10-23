.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 4b7d67c2ab2068c3ee897e90deaee72f

Starts token polling. Returns ``true`` if the start was successful (or was already active), and ``false`` otherwise.

Calling this function is not necessary in a typical use case. Once the authorization request has completed, as a result of :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.grant` call, the polling is started automatically.

This function can be useful in cases where resuming (retrying) the token polling a bit later is needed, without restarting the whole authorization flow. For example in case of a transient network connectivity loss.

Polling interval is defined by the authorization server, and is typically 5 seconds. First poll request is sent once the first interval has elapsed.

.. seealso:: polling, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.stopTokenPolling`, :ref:`qoauth2deviceauthorizationflow-device-flow-usage`.
