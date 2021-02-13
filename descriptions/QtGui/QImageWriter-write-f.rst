.. sip:method-description::
    :status: todo
    :pysig: b5207006acd9098e45a6c3737781523d
    :realsig: (const QImage&)
    :digest: be607bda6c54a4ccdbc90c6f57529fd9

Writes the image *image* to the assigned device or file name. Returns ``true`` on success; otherwise returns ``false``. If the operation fails, you can call :sip:ref:`~PyQt6.QtGui.QImageWriter.error` to find the type of error that occurred, or :sip:ref:`~PyQt6.QtGui.QImageWriter.errorString` to get a human readable description of the error.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.canWrite`, :sip:ref:`~PyQt6.QtGui.QImageWriter.error`, :sip:ref:`~PyQt6.QtGui.QImageWriter.errorString`.
