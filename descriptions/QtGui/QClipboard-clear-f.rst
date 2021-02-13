.. sip:method-description::
    :status: todo
    :pysig: 6c8a0803806937c99514a3f931788381
    :realsig: (QClipboard::Mode)
    :digest: f7599ef13ae3e7d12c2198d2c60a7578

Clear the clipboard contents.

The *mode* argument is used to control which part of the system clipboard is used. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`, this function clears the global clipboard contents. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Selection`, this function clears the global mouse selection contents. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.FindBuffer`, this function clears the search string buffer.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode`, :sip:ref:`~PyQt6.QtGui.QClipboard.supportsSelection`.
