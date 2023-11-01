.. sip:method-description::
    :status: todo
    :pysig: 8694a8502300d430953fcb3f5f4abd2c
    :realsig: (const QString&, QMetaType) const
    :digest: bc8dc3dfdaae81a09e8cdcd36a0d47d5

Returns a variant with the given *type* containing data for the MIME type specified by *mimeType*. If the object does not support the MIME type or variant type given, a null variant is returned instead.

This function is called by the general :sip:ref:`~PyQt6.QtCore.QMimeData.data` getter and by the convenience getters (\ :sip:ref:`~PyQt6.QtCore.QMimeData.text`, :sip:ref:`~PyQt6.QtCore.QMimeData.html`, :sip:ref:`~PyQt6.QtCore.QMimeData.urls`, :sip:ref:`~PyQt6.QtCore.QMimeData.imageData`, and :sip:ref:`~PyQt6.QtCore.QMimeData.colorData`). You can reimplement it if you want to store your data using a custom data structure (instead of a :sip:ref:`~PyQt6.QtCore.QByteArray`, which is what :sip:ref:`~PyQt6.QtCore.QMimeData.setData` provides). You would then also need to reimplement :sip:ref:`~PyQt6.QtCore.QMimeData.hasFormat` and :sip:ref:`~PyQt6.QtCore.QMimeData.formats`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.data`.
