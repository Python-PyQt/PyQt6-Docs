.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: a925cbe6bb3ca8d15b30a6a9d8d1a7ed

Sets the source to the *url*, loads the QML component and instantiates it.

Ensure that the URL provided is full and correct, in particular, use :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile` when loading a file from the local filesystem.

Calling this method multiple times with the same url will result in the QML component being reinstantiated.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickView.source`.
