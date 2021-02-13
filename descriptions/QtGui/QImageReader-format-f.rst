.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 11fc022c5941d1ceeda902033fe42c36

Returns the format :sip:ref:`~PyQt6.QtGui.QImageReader` uses for reading images.

You can call this function after assigning a device to the reader to determine the format of the device. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagereader.py
    :lines: 67-68

If the reader cannot read any image from the device (e.g., there is no image there, or the image has already been read), or if the format is unsupported, this function returns an empty QByteArray().

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.setFormat`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats`.
