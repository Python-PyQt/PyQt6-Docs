.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: 1ee189d1a225c8acc19133b7a959032e

Creates the directory path *dirPath*.

The function will create all parent directories necessary to create the directory.

Returns ``true`` if successful; otherwise returns ``false``.

If the path already exists when this function is called, it will return true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.rmpath`.
