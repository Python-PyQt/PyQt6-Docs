.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: e0ef651c77336a181a0a3989396d4238

Resolves an NTFS junction to the path it references.

Returns the absolute path to the directory an NTFS junction points to, or an empty string if the object is not an NTFS junction.

There is no guarantee that the directory named by the NTFS junction actually exists.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isJunction`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymbolicLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isShortcut`.
