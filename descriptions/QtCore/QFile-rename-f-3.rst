.. sip:method-description::
    :status: todo
    :pysig: 036e9c2cff75e17278911a538a7e62f1
    :realsig: (const QString&, const QString&)
    :digest: f392594f7bead9752f9ef94ec9fe22db

Renames the file *oldName* to *newName*. Returns ``true`` if successful; otherwise returns ``false``.

If a file with the name *newName* already exists, :sip:ref:`~PyQt6.QtCore.QFile.rename` returns ``false`` (i.e., :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.rename`.
