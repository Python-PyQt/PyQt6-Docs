.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: e937e56776166426b5a90778c2a42d26

Tells this handler to listen for incoming URLs. Returns ``true`` if listening is successful, and ``false`` otherwise.

The handler will match URLs to :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthUriSchemeReplyHandler.redirectUrl`. If the received URL does not match, it will be forwarded to QDesktopServices::openURL().

Active listening is only required when performing the initial authorization phase, typically initiated by a :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.grant` call.

It is recommended to close the listener after successful authorization. Listening is not needed for :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.requestAccessToken`.
