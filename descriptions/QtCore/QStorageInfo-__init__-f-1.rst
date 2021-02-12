.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 93de2d5e99cf26c847ac50e423f506a1

Constructs a new :sip:ref:`~PyQt6.QtCore.QStorageInfo` object that gives information about the volume mounted at *path*.

If you pass a directory or file, the :sip:ref:`~PyQt6.QtCore.QStorageInfo` object will refer to the volume where this directory or file is located. You can check if the created object is correct using the :sip:ref:`~PyQt6.QtCore.QStorageInfo.isValid` method.

The following example shows how to get the volume on which the application is located. It is recommended to always check that the volume is ready and valid.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qstorageinfo.py
    :lines: 54-57

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.setPath`.
