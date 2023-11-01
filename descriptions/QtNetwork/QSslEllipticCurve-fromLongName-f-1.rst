.. sip:method-description::
    :status: todo
    :pysig: 377dbe47ca175aea1abba7913de64364
    :realsig: (const QString&)
    :digest: 384f8b74e22735235bb04126546531ce

Returns an :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve` instance representing the named curve *name*. The *name* is a long name for the curve, whose exact spelling depends on the SSL implementation.

If the given *name* is not supported, returns an invalid :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve` instance.

**Note:** The OpenSSL implementation of this function treats the name case-sensitively.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve.longName`.
