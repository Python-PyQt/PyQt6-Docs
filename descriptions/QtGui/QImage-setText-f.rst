.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&,const QString&)
    :digest: 2dfb4f4cb844078ed3a54bff9ecbc07b

Sets the image text to the given *text* and associate it with the given *key*.

If you just want to store a single text block (i.e., a "comment" or just a description), you can either pass an empty key, or use a generic key like "Description".

The image text is embedded into the image data when you call :sip:ref:`~PyQt6.QtGui.QImage.save` or :sip:ref:`~PyQt6.QtGui.QImageWriter.write`.

Not all image formats support embedded text. You can find out if a specific image or format supports embedding text by using :sip:ref:`~PyQt6.QtGui.QImageWriter.supportsOption`. We give an example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-image-supportedformat.py
    :lines: 57-60

You can use :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats` to find out which image formats are available to you.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.text`, :sip:ref:`~PyQt6.QtGui.QImage.textKeys`.
