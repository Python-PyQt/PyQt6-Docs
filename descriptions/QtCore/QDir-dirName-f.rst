.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 6da5436888b09b9897e733978e27b840

Returns the name of the directory; this is *not* the same as the path, e.g. a directory with the name "mail", might have the path "/var/spool/mail". If the directory has no name (e.g. it is the root directory) an empty string is returned.

No check is made to ensure that a directory with this name actually exists; but see :sip:ref:`~PyQt6.QtCore.QDir.exists`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.path`, :sip:ref:`~PyQt6.QtCore.QDir.filePath`, :sip:ref:`~PyQt6.QtCore.QDir.absolutePath`, :sip:ref:`~PyQt6.QtCore.QDir.absoluteFilePath`.
