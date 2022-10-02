.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: d1780d50708550494ebca1ab8131d8c9

Removes the directory specified by *dirName*.

The directory must be empty for rmdir() to succeed.

Returns ``true`` if successful; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.mkdir`.
