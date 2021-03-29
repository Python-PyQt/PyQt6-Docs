.. sip:method-description::
    :status: todo
    :pysig: c8ac1c457fcb661bda5506439e38c844
    :realsig: (QImageIOHandler::ImageOption) const
    :digest: e427d2a324bbe37311f291ecfc8c4e1c

Returns ``true`` if the writer supports *option*; otherwise returns false.

Different image formats support different options. Call this function to determine whether a certain option is supported by the current format. For example, the PNG format allows you to embed text into the image's metadata (see text()).

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagewriter.py
    :lines: 83-85

Options can be tested after the writer has been associated with a format.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.supportsOption`, :sip:ref:`~PyQt6.QtGui.QImageWriter.setFormat`.
