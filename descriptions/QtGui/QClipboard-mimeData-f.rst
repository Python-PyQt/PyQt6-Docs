.. sip:method-description::
    :status: todo
    :pysig: 4732bfe5d0936ff2e7ca83a6e3e168f4
    :realsig: (QClipboard::Mode) const
    :digest: 1dd0b40f24c5918ab4c55f96e6fe6442

Returns a pointer to a :sip:ref:`~PyQt6.QtCore.QMimeData` representation of the current clipboard data (can be ``nullptr`` if the given *mode* is not supported by the platform).

The *mode* argument is used to control which part of the system clipboard is used. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`, the data is retrieved from the global clipboard. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Selection`, the data is retrieved from the global mouse selection. If *mode* is :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.FindBuffer`, the data is retrieved from the search string buffer.

The :sip:ref:`~PyQt6.QtGui.QClipboard.text`, :sip:ref:`~PyQt6.QtGui.QClipboard.image`, and :sip:ref:`~PyQt6.QtGui.QClipboard.pixmap` functions are simpler wrappers for retrieving text, image, and pixmap data.

**Note:** The pointer returned might become invalidated when the contents of the clipboard changes; either by calling one of the setter functions or externally by the system clipboard changing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QClipboard.setMimeData`.
