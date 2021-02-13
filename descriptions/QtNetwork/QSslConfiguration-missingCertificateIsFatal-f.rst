.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ccee01321fbd4da7908a40ea7eb96bbe

Returns true if errors with code :sip:ref:`~PyQt6.QtNetwork.QSslError.SslError.NoPeerCertificate` cannot be ignored.

**Note:** Always returns false for all TLS backends but OpenSSL.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setMissingCertificateIsFatal`.
