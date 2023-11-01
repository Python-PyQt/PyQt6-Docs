.. sip:method-description::
    :status: todo
    :pysig: 21031ffd0e34ae30fb5d92724a5c7c8b
    :realsig: (const QDir&, const QString&)
    :digest: 6fa6457a4402a1596b4e3b1b635b26e8

Constructs a new :sip:ref:`~PyQt6.QtCore.QFileInfo` that gives information about the given *file* relative to the directory *dir*.

If *dir* has a relative path, the :sip:ref:`~PyQt6.QtCore.QFileInfo` will also have a relative path.

If *file* is an absolute path, then the directory specified by *dir* will be disregarded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
