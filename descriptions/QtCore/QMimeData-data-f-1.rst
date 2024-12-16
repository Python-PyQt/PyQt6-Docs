.. sip:method-description::
    :status: todo
    :pysig: 2cc60dc07b2ee3a107348d61c248bd49
    :realsig: (const QString&) const
    :digest: 7599cd936d80504bc89ae8ad45462ef3

Returns the data stored in the object in the format described by the MIME type specified by *mimeType*. If this object does not contain data for the *mimeType* MIME type (see :sip:ref:`~PyQt6.QtCore.QMimeData.hasFormat`), this function may perform a best effort conversion to it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.hasFormat`, :sip:ref:`~PyQt6.QtCore.QMimeData.setData`.
