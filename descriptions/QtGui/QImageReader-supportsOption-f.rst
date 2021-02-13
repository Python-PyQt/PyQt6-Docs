.. sip:method-description::
    :status: todo
    :pysig: c8ac1c457fcb661bda5506439e38c844
    :realsig: (QImageIOHandler::ImageOption) const
    :digest: a041a47722fe35186b6e58c8953ff00f

Returns ``true`` if the reader supports *option*; otherwise returns false.

Different image formats support different options. Call this function to determine whether a certain option is supported by the current format. For example, the PNG format allows you to embed text into the image's metadata (see :sip:ref:`~PyQt6.QtGui.QImageReader.text`), and the BMP format allows you to determine the image's size without loading the whole image into memory (see :sip:ref:`~PyQt6.QtGui.QImageReader.size`).

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagereader.py
    :lines: 88-90

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.supportsOption`.
