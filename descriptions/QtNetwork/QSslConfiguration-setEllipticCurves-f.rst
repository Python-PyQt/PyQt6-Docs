.. sip:method-description::
    :status: todo
    :pysig: a7fba361f7f6d515e8db6e8ba8e06a95
    :realsig: (const QList<QSslEllipticCurve>&)
    :digest: 44f2ec3f8449d9596575f9813f61491a

Sets the list of elliptic curves to be used by this socket to *curves*, which must contain a subset of the curves in the list returned by :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedEllipticCurves`.

Restricting the elliptic curves must be done before the handshake phase, where the session cipher is chosen.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ellipticCurves`.
