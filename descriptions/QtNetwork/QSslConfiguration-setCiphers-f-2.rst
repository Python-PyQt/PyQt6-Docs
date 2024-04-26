.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 087db1f0f08caacabb9391fd6adb6468

Sets the cryptographic cipher suite for this configuration to *ciphers*, which is a colon-separated list of cipher suite names. The ciphers are listed in order of preference, starting with the most preferred cipher. Each cipher name in *ciphers* must be the name of a cipher in the list returned by :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`. Restricting the cipher suite must be done before the handshake phase, where the session cipher is chosen.

**Note:** With the Schannel backend the order of the ciphers is ignored and Schannel picks the most secure one during the handshake.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ciphers`.
