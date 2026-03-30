.. sip:method-description::
    :status: todo
    :pysig: 4ea494623157eb10b866f94d53018fdb
    :realsig: (const QDir&, const QString&)
    :digest: 686097a8f14056e03c44f5b5f8762c47

Sets the path of the file system entry that this :sip:ref:`~PyQt6.QtCore.QFileInfo` provides information about to *path* in directory *dir*.

If *dir* has a relative path, the :sip:ref:`~PyQt6.QtCore.QFileInfo` will also have a relative path.

If *path* is absolute, then the directory specified by *dir* will be disregarded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
