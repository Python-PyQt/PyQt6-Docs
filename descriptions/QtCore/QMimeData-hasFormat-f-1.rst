.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&) const
    :digest: 29444d931a4dea5c4d8d9d5156efb8f2

Returns ``true`` if the object can return data for the MIME type specified by *mimeType*; otherwise returns ``false``.

For the most common types of data, you can call the higher-level functions :sip:ref:`~PyQt6.QtCore.QMimeData.hasText`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasHtml`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasUrls`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasImage`, and :sip:ref:`~PyQt6.QtCore.QMimeData.hasColor` instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.formats`, :sip:ref:`~PyQt6.QtCore.QMimeData.setData`, :sip:ref:`~PyQt6.QtCore.QMimeData.data`.
