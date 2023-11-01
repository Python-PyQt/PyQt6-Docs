.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 3f100c1c346f2d92a79135b54031a8d8

Sets the cryptographic cipher suite for this configuration to *ciphers*, which is a colon-separated list of cipher suite names. The ciphers are listed in order of preference, starting with the most preferred cipher. For example:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslconfiguration.py
    :lines: 61-62

Each cipher name in *ciphers* must be the name of a cipher in the list returned by :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`. Restricting the cipher suite must be done before the handshake phase, where the session cipher is chosen.

**Note:** This is not currently supported in the Schannel backend.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ciphers`.
