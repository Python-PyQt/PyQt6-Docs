.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: 9fd3053acfd2736c9f4d0784ff33abd9

Removes the directory path *dirPath*.

The function will remove all parent directories in *dirPath*, provided that they are empty. This is the opposite of mkpath(dirPath).

Returns ``true`` if successful; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.mkpath`.
