.. sip:method-description::
    :status: todo
    :pysig: 4f506bf52b8228bac582de7fa1b48756
    :realsig: () const
    :digest: b2c370831ddb0b71c2d4567a3b19062d

Returns this connection's CA certificate database. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate. It can be modified prior to the handshake with :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCaCertificates`, or with :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificate` and :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificates`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCaCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificates`.
