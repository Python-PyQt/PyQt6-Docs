.. sip:method-description::
    :status: todo
    :pysig: da403e299845f8c1b31972a05bd0f8ae
    :realsig: (const QString&,const QString&)
    :digest: 1937f68e2ad3b0e504d0dc35e455f32b

This is an overloaded function.

Copies the file named *fileName* to *newName*.

This file is closed before it is copied.

If the copied file is a symbolic link (symlink), the file it refers to is copied, not the link itself. With the exception of permissions, which are copied, no other file metadata is copied.

Returns ``true`` if successful; otherwise returns ``false``.

Note that if a file with the name *newName* already exists, :sip:ref:`~PyQt6.QtCore.QFile.copy` returns ``false``. This means :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.rename`.
