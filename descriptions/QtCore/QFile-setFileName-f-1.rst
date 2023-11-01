.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 4fa214ba3774bdf5c20a11516cba9aea

Sets the *name* of the file. The name can have no path, a relative path, or an absolute path.

Do not call this function if the file has already been opened.

If the file name has no path or a relative path, the path used will be the application's current directory path *at the time of the :sip:ref:`~PyQt6.QtCore.QFile.open`* call.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfile.py
    :lines: 54-58

Note that the directory separator "/" works for all operating systems supported by Qt.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo`, :sip:ref:`~PyQt6.QtCore.QDir`.
