.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: e67f16e5f07de5717f6ad6fd7399f4bb

Allows or disallows the origin. Setting *allowed* to true, will accept the connection request for the given origin.

Setting *allowed* to false, will reject the connection request.

**Note:** By default, all origins are accepted.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketCorsAuthenticator.allowed`.
