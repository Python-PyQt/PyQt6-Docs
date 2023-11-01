.. sip:method-description::
    :status: todo
    :pysig: 6fb60876b5136c816ecc1a895d3012c0
    :realsig: (const QString&, const QString&)
    :digest: 0586ca76afec1b552336a601c7e1b174

Sets the image text associated with the key *key* to *text*. This is useful for storing copyright information or other information about the image. Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagewriter.py
    :lines: 70-73

If you want to store a single block of data (e.g., a comment), you can pass an empty key, or use a generic key like "Description".

The key and text will be embedded into the image data after calling :sip:ref:`~PyQt6.QtGui.QImageWriter.write`.

Support for this option is implemented through :sip:ref:`~PyQt6.QtGui.QImageIOHandler.ImageOption.Description`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setText`, :sip:ref:`~PyQt6.QtGui.QImageReader.text`.
