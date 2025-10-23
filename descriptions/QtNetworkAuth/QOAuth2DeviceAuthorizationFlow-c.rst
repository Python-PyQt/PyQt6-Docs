.. sip:class-description::
    :status: todo
    :brief: Implementation of the Device Authorization Grant flow
    :digest: 2b086aa5b5ae76bbf1df8bae72dabd34

The :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow` class provides an implementation of the `Device Authorization Grant <https://datatracker.ietf.org/doc/html/rfc8628>`_ flow.

This class implements the `Device Authorization Grant <https://datatracker.ietf.org/doc/html/rfc8628>`_ flow, which is used to obtain and refresh access tokens and ID tokens, particularly on devices lacking a user-agent or with limited input capabilities. These devices include televisions, machine HMIs, appliances, and IoT devices.

Device flow can be used on any platform and operating system that is capable of SSL/TLS requests. Unlike :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow`, this flow is not based on redirects, and therefore does not use a :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler`.

.. _qoauth2deviceauthorizationflow-device-flow-usage:

Device Flow Usage
-----------------

The following snippets illustrate the typical usage. First, we set up the flow similarly to :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow`:

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py

Then we connect to :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.authorizeWithUserCode` signal to handle the user authorization:

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py

This part is crucial to the flow, and how you handle it depends on your specific use case. One way or another, the user needs to complete the authorization.

Device flow does not define how this authorization completion is done, making it versatile for different use cases. This can be achieved by displaying the verification URI and user code to the user, who can then navigate to it on another device. Alternatively, you could present a QR code for the user to scan with their mobile device, send to a companion application, email to the user, and so on.

While authorization is pending, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow` polls the server at specific intervals (typically 5 seconds) until the user accepts or rejects the authorization, upon which the server responds accordingly and the flow concludes.

Errors can be detected as follows:

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py

:sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.serverReportedErrorOccurred` signal can be used to get information on specific RFC-defined errors. However, unlike :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.requestFailed`, it doesn't cover errors such as network errors or client configuration errors.

Flow completion is detected similarly as with :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow`, for example:

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py
