.. sip:method-description::
    :status: todo
    :pysig: 3b7c385391acbd00dbe2f1aafdce8d81
    :realsig: (const QDir&,const QString&)
    :digest: 6fa6457a4402a1596b4e3b1b635b26e8

Constructs a new :sip:ref:`~PyQt6.QtCore.QFileInfo` that gives information about the given *file* relative to the directory *dir*.

If *dir* has a relative path, the :sip:ref:`~PyQt6.QtCore.QFileInfo` will also have a relative path.

If *file* is an absolute path, then the directory specified by *dir* will be disregarded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
