.. sip:method-description::
    :status: todo
    :pysig: 0bd5b2e1d97821094eb31d9a7e0c951c
    :realsig: (const QUrlQuery&)
    :digest: f960424ecea93e7a8f5c5c550e8262a8

Sets the query string of the URL to *query*.

This function reconstructs the query string from the :sip:ref:`~PyQt6.QtCore.QUrlQuery` object and sets on this :sip:ref:`~PyQt6.QtCore.QUrl` object. This function does not have parsing parameters because the :sip:ref:`~PyQt6.QtCore.QUrlQuery` contains data that is already parsed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.query`, :sip:ref:`~PyQt6.QtCore.QUrl.hasQuery`.
