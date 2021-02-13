.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: a475d9da4224d423e54668898a9ca647

Sets the *filters* used in the file dialog, from a list of MIME types.

Convenience method for :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setNameFilters`. Uses :sip:ref:`~PyQt6.QtCore.QMimeType` to create a name filter from the glob patterns and description defined in each MIME type.

Use application/octet-stream for the "All files (\*)" filter, since that is the base MIME type for all files.

Calling  overrides any previously set name filters, and changes the return value of :sip:ref:`~PyQt6.QtWidgets.QFileDialog.nameFilters`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 135-142

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.mimeTypeFilters`.
