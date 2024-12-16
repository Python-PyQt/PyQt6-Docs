.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 2e03e3a8200c0f7c6ab58bec15b2e2a5

Saves the contents to the file and format specified by *url*.

The file extension in *url* specifies the file format (as determined by :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForUrl`).

**Note:** You can save only to a :sip:ref:`~PyQt6.QtCore.QUrl.isLocalFile`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickTextDocument.source`, :sip:ref:`~PyQt6.QtQuick.QQuickTextDocument.save`.
