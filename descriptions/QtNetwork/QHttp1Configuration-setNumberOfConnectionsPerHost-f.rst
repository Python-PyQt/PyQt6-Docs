.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: c79e73f6c733004ed9a6a671109b9984

Sets the number of connections (minimum: 1; maximum: 255) used per http(s) *host*:\ *port* combination to *number*.

If *number* is ≤ 0, does nothing. If *number* is > 255, 255 is used.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttp1Configuration.numberOfConnectionsPerHost`.
