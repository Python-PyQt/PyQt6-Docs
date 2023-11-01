.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 4c44244016fc3744faf9c383aeb6ac38

Sets the format :sip:ref:`~PyQt6.QtGui.QImageWriter` will use when writing images, to *format*. *format* is a case insensitive text string. Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagewriter.py
    :lines: 60-61

You can call :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats` for the full list of formats :sip:ref:`~PyQt6.QtGui.QImageWriter` supports.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.format`.
