.. sip:method-description::
    :status: todo
    :pysig: 02d0e34b1b6d74f491b8f2e59bd96367
    :realsig: (const QString&,qint64)
    :digest: 0c43d1b40098c4bd833a7614aa337228

This is an overloaded function.

Sets *fileName* to size (in bytes) *sz*. Returns ``true`` if the resize succeeds; false otherwise. If *sz* is larger than *fileName* currently is the new bytes will be set to 0, if *sz* is smaller the file is simply truncated.

**Warning:** This function can fail if the file doesn't exist.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.resize`.
