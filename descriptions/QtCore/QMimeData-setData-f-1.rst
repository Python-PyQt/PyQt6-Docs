.. sip:method-description::
    :status: todo
    :pysig: 1a8434e8110f782053a030b6b3fe693c
    :realsig: (const QString&, const QByteArray&)
    :digest: d9a095885efd71ead5e12b73fdb7dbed

Sets the data associated with the MIME type given by *mimeType* to the specified *data*.

For the most common types of data, you can call the higher-level functions :sip:ref:`~PyQt6.QtCore.QMimeData.setText`, :sip:ref:`~PyQt6.QtCore.QMimeData.setHtml`, :sip:ref:`~PyQt6.QtCore.QMimeData.setUrls`, :sip:ref:`~PyQt6.QtCore.QMimeData.setImageData`, and :sip:ref:`~PyQt6.QtCore.QMimeData.setColorData` instead.

Note that if you want to use a custom data type in an item view drag and drop operation, you must register it as a Qt :sip:ref:`~PyQt6.QtCore.QMetaType`, using the Q_DECLARE_METATYPE() macro, and implement stream operators for it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.data`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasFormat`, :sip:ref:`~PyQt6.QtCore.QMetaType`, Q_DECLARE_METATYPE().
