.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 6056b59d8a2f06f6fef47c92c408c5a1

Returns the canonical path, i.e. a path without symbolic links or redundant "." or ".." elements.

On systems that do not have symbolic links this function will always return the same string that :sip:ref:`~PyQt6.QtCore.QDir.absolutePath` returns. If the canonical path does not exist (normally due to dangling symbolic links)  returns an empty string.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 101-109

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.path`, :sip:ref:`~PyQt6.QtCore.QDir.absolutePath`, :sip:ref:`~PyQt6.QtCore.QDir.exists`, :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`, :sip:ref:`~PyQt6.QtCore.QDir.dirName`, :sip:ref:`~PyQt6.QtCore.QDir.absoluteFilePath`.
