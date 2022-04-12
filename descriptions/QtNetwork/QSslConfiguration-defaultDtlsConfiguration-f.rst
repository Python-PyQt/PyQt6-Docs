.. sip:method-description::
    :status: todo
    :pysig: 441afb0c9c0efa1cb39dec63993d55f1
    :realsig: ()
    :digest: 76df2f0e8b09e6e97c32028d3829e52b

Returns the default DTLS configuration to be used in new DTLS connections.

The default DTLS configuration consists of:

* no local certificate and no private key

* protocol DtlsV1_2OrLater

* the system's default CA certificate list

* the cipher list equal to the list of the SSL libraries' supported TLS 1.2 ciphers that use 128 or more secret bits for the cipher.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setDefaultDtlsConfiguration`.
