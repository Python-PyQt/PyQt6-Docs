.. sip:method-description::
    :status: todo
    :pysig: 036e9c2cff75e17278911a538a7e62f1
    :realsig: (const QString&, const QString&)
    :digest: 7c88f1ac20212c155511b8a02febbcd5

Creates a link named *linkName* that points to the file *fileName*. What a link is depends on the underlying filesystem (be it a shortcut on Windows or a symbolic link on Unix). Returns ``true`` if successful; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.link`.
