.. sip:method-description::
    :status: todo
    :pysig: 621c2783dc0326108844380798fad5cd
    :realsig: (const QPixmap&,QClipboard::Mode)
    :digest: 6c9b8c616c97fa30291d756e5a650463

Copies *pixmap* into the clipboard. Note that this is slower than :sip:ref:`~PyQt6.QtGui.QClipboard.setImage` because it needs to convert the :sip:ref:`~PyQt6.QtGui.QPixmap` to a :sip:ref:`~PyQt6.QtGui.QImage` first.

The *mode* argument is used to control which part of the system clipboard is used. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`, the pixmap is stored in the global clipboard. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Selection`, the pixmap is stored in the global mouse selection.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QClipboard.pixmap`, :sip:ref:`~PyQt6.QtGui.QClipboard.setImage`, :sip:ref:`~PyQt6.QtGui.QClipboard.setMimeData`.
