.. sip:method-description::
    :status: todo
    :pysig: 3b7c385391acbd00dbe2f1aafdce8d81
    :realsig: (const QDir&,const QString&)
    :digest: 12562c7ae54de27331a7b922413c3af7

This is an overloaded function.

Sets the path of the file system entry that this :sip:ref:`~PyQt6.QtCore.QFileInfo` provides information about to *path* in directory *dir*.

If *dir* has a relative path, the :sip:ref:`~PyQt6.QtCore.QFileInfo` will also have a relative path.

If *path* is absolute, then the directory specified by *dir* will be disregarded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
