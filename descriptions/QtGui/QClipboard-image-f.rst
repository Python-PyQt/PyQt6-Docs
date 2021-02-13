.. sip:method-description::
    :status: todo
    :pysig: 7ba64f0066fed20d6775670dea1246a3
    :realsig: (QClipboard::Mode) const
    :digest: 77eea2673eec7e345b1384475e335c0a

Returns the clipboard image, or returns a null image if the clipboard does not contain an image or if it contains an image in an unsupported image format.

The *mode* argument is used to control which part of the system clipboard is used. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`, the image is retrieved from the global clipboard. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Selection`, the image is retrieved from the global mouse selection.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QClipboard.setImage`, :sip:ref:`~PyQt6.QtGui.QClipboard.pixmap`, :sip:ref:`~PyQt6.QtGui.QClipboard.mimeData`, :sip:ref:`~PyQt6.QtGui.QImage.isNull`.
