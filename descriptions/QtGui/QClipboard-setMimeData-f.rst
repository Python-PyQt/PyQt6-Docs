.. sip:method-description::
    :status: todo
    :pysig: d3fd1bb7cf66a5246465f1d4590f741f
    :realsig: (QMimeData*,QClipboard::Mode)
    :digest: 104a4747875ac1ba8ba2b8230d5a0d97

Sets the clipboard data to *src*. Ownership of the data is transferred to the clipboard. If you want to remove the data either call :sip:ref:`~PyQt6.QtGui.QClipboard.clear` or call  again with new data.

The *mode* argument is used to control which part of the system clipboard is used. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`, the data is stored in the global clipboard. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Selection`, the data is stored in the global mouse selection. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.FindBuffer`, the data is stored in the search string buffer.

The :sip:ref:`~PyQt6.QtGui.QClipboard.setText`, :sip:ref:`~PyQt6.QtGui.QClipboard.setImage` and :sip:ref:`~PyQt6.QtGui.QClipboard.setPixmap` functions are simpler wrappers for setting text, image and pixmap data respectively.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QClipboard.mimeData`.
