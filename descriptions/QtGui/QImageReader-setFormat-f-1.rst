.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 30addf904b0e04b058af9aed1e191cba

Sets the format :sip:ref:`~PyQt6.QtGui.QImageReader` will use when reading images, to *format*. *format* is a case insensitive text string. Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagereader.py
    :lines: 59-60

You can call :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats` for the full list of formats :sip:ref:`~PyQt6.QtGui.QImageReader` supports.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.format`.
