.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&)
    :digest: 48bfaa53b1d2f7493a827d228e485a24

Copies the file currently specified by :sip:ref:`~PyQt6.QtCore.QFile.fileName` to a file called *newName*. Returns ``true`` if successful; otherwise returns ``false``.

Note that if a file with the name *newName* already exists,  returns ``false`` (i.e. :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it).

The source file is closed before it is copied.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.setFileName`.
