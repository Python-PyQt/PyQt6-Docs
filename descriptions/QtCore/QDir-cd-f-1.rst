.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 0af70140085b12da03f481c8868306ab

Changes the :sip:ref:`~PyQt6.QtCore.QDir`'s directory to *dirName*.

Returns ``true`` if the new directory exists; otherwise returns ``false``. Note that the logical cd() operation is not performed if the new directory does not exist.

Calling cd("..") is equivalent to calling :sip:ref:`~PyQt6.QtCore.QDir.cdUp`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.cdUp`, :sip:ref:`~PyQt6.QtCore.QDir.isReadable`, :sip:ref:`~PyQt6.QtCore.QDir.exists`, :sip:ref:`~PyQt6.QtCore.QDir.path`.
