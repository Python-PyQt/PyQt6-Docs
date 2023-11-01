.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&) const
    :digest: 9fd3053acfd2736c9f4d0784ff33abd9

Removes the directory path *dirPath*.

The function will remove all parent directories in *dirPath*, provided that they are empty. This is the opposite of mkpath(dirPath).

Returns ``true`` if successful; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.mkpath`.
