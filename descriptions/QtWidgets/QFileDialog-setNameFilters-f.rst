.. sip:method-description::
    :status: todo
    :pysig: 252f2463b17d7b65060495677c920d4c
    :realsig: (const QStringList&)
    :digest: 298cd5c77a0593da9710026037652681

Sets the *filters* used in the file dialog.

Note that the filter **\*.\*** is not portable, because the historical assumption that the file extension determines the file type is not consistent on every operating system. It is possible to have a file with no dot in its name (for example, ``Makefile``). In a native Windows file dialog, **\*.\*** matches such files, while in other types of file dialogs it might not match. So, it's better to use **\*** if you mean to select any file.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 94-100

:sip:ref:`~PyQt6.QtWidgets.QFileDialog.setMimeTypeFilters` has the advantage of providing all possible name filters for each file type. For example, JPEG images have three possible extensions; if your application can open such files, selecting the ``image/jpeg`` mime type as a filter allows you to open all of them.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.nameFilters`.
