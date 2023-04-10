.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 9d642455835d8bbbf612480594ed4912

Changes directory by moving one directory up from the :sip:ref:`~PyQt6.QtCore.QDir`'s current directory.

Returns ``true`` if the new directory exists; otherwise returns ``false``. Note that the logical cdUp() operation is not performed if the new directory does not exist.

**Note:** On Android, this is not supported for content URIs. For more information, see `DocumentFile.getParentFile() <https://doc.qt.io/qt-6/https://developer.android.com/reference/androidx/documentfile/provider/DocumentFile#getParentFile()>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.cd`, :sip:ref:`~PyQt6.QtCore.QDir.isReadable`, :sip:ref:`~PyQt6.QtCore.QDir.exists`, :sip:ref:`~PyQt6.QtCore.QDir.path`.
