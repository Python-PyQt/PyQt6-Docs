.. sip:method-description::
    :status: todo
    :pysig: 466247a13f2d4025eda7edfadec20625
    :realsig: () const
    :digest: 02de539520cfde6a2ad4511691bf8b44

Returns the list of HTTP Strict Transport Security policies. This list can differ from what was initially set via :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.addStrictTransportSecurityHosts` if HSTS cache was updated from a "Strict-Transport-Security" response header.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.addStrictTransportSecurityHosts`, :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy`.
