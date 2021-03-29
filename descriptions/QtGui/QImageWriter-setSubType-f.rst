.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: 376d604199799f09c81d2233e758ca57

This is an image format specific function that sets the subtype of the image to *type*. Subtype can be used by a handler to determine which format it should use while saving the image.

For example, saving an image in DDS format with A8R8G8R8 subtype:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagewriter.py
    :lines: 95-98

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.subType`.
