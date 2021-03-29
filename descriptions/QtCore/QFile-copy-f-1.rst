.. sip:method-description::
    :status: todo
    :pysig: da403e299845f8c1b31972a05bd0f8ae
    :realsig: (const QString&,const QString&)
    :digest: 76f7da5b505e21659dfb1efcb09360fb

This is an overloaded function.

Copies the file *fileName* to *newName*. Returns ``true`` if successful; otherwise returns ``false``.

If a file with the name *newName* already exists, :sip:ref:`~PyQt6.QtCore.QFile.copy` returns ``false`` (i.e., :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.rename`.
