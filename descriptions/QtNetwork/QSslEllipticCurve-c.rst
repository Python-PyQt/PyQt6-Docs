.. sip:class-description::
    :status: todo
    :brief: Represents an elliptic curve for use by elliptic-curve cipher algorithms
    :digest: 41b42620b184977ca3845ae10ba45a7e

Represents an elliptic curve for use by elliptic-curve cipher algorithms.

The class :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve` represents an elliptic curve for use by elliptic-curve cipher algorithms.

Elliptic curves can be constructed from a "short name" (SN) (\ :sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve.fromShortName`), and by a call to :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedEllipticCurves`.

:sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve` instances can be compared for equality and can be used as keys in `QHash <https://doc.qt.io/qt-6/qhash-proxy.html>`_ and QSet. They cannot be used as key in a QMap.

**Note:** This class is currently only supported in OpenSSL.
