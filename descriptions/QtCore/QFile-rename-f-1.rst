.. sip:method-description::
    :status: todo
    :pysig: da403e299845f8c1b31972a05bd0f8ae
    :realsig: (const QString&,const QString&)
    :digest: 10bd746112dfc3ea4c36491363ff38d0

This is an overloaded function.

Renames the file *oldName* to *newName*. Returns ``true`` if successful; otherwise returns ``false``.

If a file with the name *newName* already exists, :sip:ref:`~PyQt6.QtCore.QFile.rename` returns ``false`` (i.e., :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.rename`.
