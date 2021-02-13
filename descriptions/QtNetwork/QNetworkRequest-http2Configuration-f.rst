.. sip:method-description::
    :status: todo
    :pysig: a9fa1c44738322cc9870d2145d198e5d
    :realsig: () const
    :digest: 2a9598a34111d48006a4820d8fa9a216

Returns the current parameters that :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` is using for this request and its underlying HTTP/2 connection. This is either a configuration previously set by an application or a default configuration.

The default values that :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` is using are:

* Window size for connection-level flowcontrol is 2147483647 octets

* Window size for stream-level flowcontrol is 21474836 octets

* Max frame size is 16384

By default, server push is disabled, Huffman compression and string indexing are enabled.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setHttp2Configuration`.
