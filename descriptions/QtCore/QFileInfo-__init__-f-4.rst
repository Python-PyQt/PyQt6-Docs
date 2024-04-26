.. sip:method-description::
    :status: todo
    :pysig: 3b7c385391acbd00dbe2f1aafdce8d81
    :realsig: (const QDir&,const QString&)
    :digest: 3c3f36601c468eef8acd05aaea7b7faa

Constructs a new :sip:ref:`~PyQt6.QtCore.QFileInfo` that gives information about the given file system entry *path* that is relative to the directory *dir*.

If *dir* has a relative path, the :sip:ref:`~PyQt6.QtCore.QFileInfo` will also have a relative path.

If *path* is absolute, then the directory specified by *dir* will be disregarded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
