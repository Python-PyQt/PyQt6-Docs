.. sip:method-description::
    :status: todo
    :pysig: a9fa1c44738322cc9870d2145d198e5d
    :realsig: (const QHttp2Configuration&)
    :digest: 4d231d0d311d42933586c31f63c1a8ae

Sets request's HTTP/2 parameters from *configuration*.

**Note:** The configuration must be set prior to making a request.

**Note:** HTTP/2 multiplexes several streams in a single HTTP/2 connection. This implies that :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will use the configuration found in the first request from a series of requests sent to the same host.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.http2Configuration`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QHttp2Configuration`.
