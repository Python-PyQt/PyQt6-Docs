.. sip:method-description::
    :status: todo
    :pysig: 2e1e4fde32fc7292dbe8e18ea768734a
    :realsig: (const QStringList&)
    :digest: 85e027d4b09f474b8aea0642830f4914

Sets the *filters* used in the file dialog, from a list of MIME types.

Convenience method for :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setNameFilters`. Uses :sip:ref:`~PyQt6.QtCore.QMimeType` to create a name filter from the glob patterns and description defined in each MIME type.

Use application/octet-stream for the "All files (\*)" filter, since that is the base MIME type for all files.

Calling setMimeTypeFilters overrides any previously set name filters, and changes the return value of :sip:ref:`~PyQt6.QtWidgets.QFileDialog.nameFilters`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 135-142

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.mimeTypeFilters`.
