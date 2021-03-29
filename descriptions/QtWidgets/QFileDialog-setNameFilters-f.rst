.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 298cd5c77a0593da9710026037652681

Sets the *filters* used in the file dialog.

Note that the filter **\*.\*** is not portable, because the historical assumption that the file extension determines the file type is not consistent on every operating system. It is possible to have a file with no dot in its name (for example, ``Makefile``). In a native Windows file dialog, **\*.\*** will match such files, while in other types of file dialogs it may not. So it is better to use **\*** if you mean to select any file.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 94-100

:sip:ref:`~PyQt6.QtWidgets.QFileDialog.setMimeTypeFilters` has the advantage of providing all possible name filters for each file type. For example, JPEG images have three possible extensions; if your application can open such files, selecting the ``image/jpeg`` mime type as a filter will allow you to open all of them.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.nameFilters`.
