.. sip:class-description::
    :status: todo
    :brief: Controls HTTP/2 parameters and settings
    :digest: ee75036f9d0b96dc6a6270e0e705d35c

The :sip:ref:`~PyQt6.QtNetwork.QHttp2Configuration` class controls HTTP/2 parameters and settings.

:sip:ref:`~PyQt6.QtNetwork.QHttp2Configuration` controls HTTP/2 parameters and settings that :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will use to send requests and process responses when the HTTP/2 protocol is enabled.

The HTTP/2 parameters that :sip:ref:`~PyQt6.QtNetwork.QHttp2Configuration` currently supports include:

* The session window size for connection-level flow control. Will be sent to a remote peer when needed as 'WINDOW_UPDATE' frames on the stream with an identifier 0.

* The stream receiving window size for stream-level flow control. Sent as 'SETTINGS_INITIAL_WINDOW_SIZE' parameter in the initial SETTINGS frame and, when needed, 'WINDOW_UPDATE' frames will be sent on streams that :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` opens.

* The maximum frame size. This parameter limits the maximum payload a frame coming from the remote peer can have. Sent by :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` as 'SETTINGS_MAX_FRAME_SIZE' parameter in the initial 'SETTINGS' frame.

* The server push. Allows to enable or disable server push. Sent as 'SETTINGS_ENABLE_PUSH' parameter in the initial 'SETTINGS' frame.

The :sip:ref:`~PyQt6.QtNetwork.QHttp2Configuration` class also controls if the header compression algorithm (HPACK) is additionally using Huffman coding for string compression.

**Note:** The configuration must be set before the first request was sent to a given host (and thus an HTTP/2 session established).

**Note:** Details about flow control, server push and 'SETTINGS' can be found in `RFC 7540 <https://httpwg.org/specs/rfc7540.html>`_. Different modes and parameters of the HPACK compression algorithm are described in `RFC 7541 <https://httpwg.org/specs/rfc7541.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setHttp2Configuration`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.http2Configuration`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.
