.. sip:method-description::
    :status: todo
    :pysig: 7e28879cb589320315d2e4999164418a
    :realsig: (QFile&)
    :digest: 70eb99102f8a8e237ef8ad40b4967a6b

If *file* is not already a native file, then a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` is created in :sip:ref:`~PyQt6.QtCore.QDir.tempPath`, the contents of *file* is copied into it, and a pointer to the temporary file is returned. Does nothing and returns ``0`` if *file* is already a native file.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtemporaryfile.py
    :lines: 68-72

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isNativePath`.
