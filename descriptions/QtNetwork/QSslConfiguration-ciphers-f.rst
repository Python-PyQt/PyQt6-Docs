.. sip:method-description::
    :status: todo
    :pysig: d3cde2863048dc2165a62d3894eaa11d
    :realsig: () const
    :digest: 4a0729851654c59c949d4c5db550522a

Returns this connection's current cryptographic cipher suite. This list is used during the handshake phase for choosing a session cipher. The returned list of ciphers is ordered by descending preference. (i.e., the first cipher in the list is the most preferred cipher). The session cipher will be the first one in the list that is also supported by the peer.

By default, the handshake phase can choose any of the ciphers supported by this system's SSL libraries, which may vary from system to system. The list of ciphers supported by this system's SSL libraries is returned by :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`. You can restrict the list of ciphers used for choosing the session cipher for this socket by calling :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCiphers` with a subset of the supported ciphers. You can revert to using the entire set by calling :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCiphers` with the list returned by :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`.

**Note:** This is not currently supported in the Schannel backend.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCiphers`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`.
