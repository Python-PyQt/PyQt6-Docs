.. sip:method-description::
    :status: todo
    :pysig: 441afb0c9c0efa1cb39dec63993d55f1
    :realsig: ()
    :digest: b3036b660bad31d0de85c72eab57a214

Returns the default SSL configuration to be used in new SSL connections.

The default SSL configuration consists of:

* no local certificate and no private key

* protocol :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol.SecureProtocols`

* the system's default CA certificate list

* the cipher list equal to the list of the SSL libraries' supported SSL ciphers that are 128 bits or more

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setDefaultConfiguration`.
