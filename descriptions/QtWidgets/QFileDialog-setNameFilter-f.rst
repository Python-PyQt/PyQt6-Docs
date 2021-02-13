.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 060729e20b5d12e58176348a8d3e2929

Sets the filter used in the file dialog to the given *filter*.

If *filter* contains a pair of parentheses containing one or more filename-wildcard patterns, separated by spaces, then only the text contained in the parentheses is used as the filter. This means that these calls are all equivalent:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 88-89

**Note:** With Android's native file dialog, the mime type matching the given name filter is used because only mime types are supported.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setMimeTypeFilters`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setNameFilters`.
