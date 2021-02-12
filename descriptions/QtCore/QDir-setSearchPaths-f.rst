.. sip:method-description::
    :status: todo
    :pysig: b754924ab813f5e3b3453efcce84d25c
    :realsig: (const QString&,const QStringList&)
    :digest: cad945109c03a0487831b6ad994d037a

Sets or replaces Qt's search paths for file names with the prefix *prefix* to *searchPaths*.

To specify a prefix for a file name, prepend the prefix followed by a single colon (e.g., "images:undo.png", "xmldocs:books.xml"). *prefix* can only contain letters or numbers (e.g., it cannot contain a colon, nor a slash).

Qt uses this search path to locate files with a known prefix. The search path entries are tested in order, starting with the first entry.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 123-127

File name prefix must be at least 2 characters long to avoid conflicts with Windows drive letters.

Search paths may contain paths to `The Qt Resource System <https://doc.qt.io/qt-6/resources.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.searchPaths`.
