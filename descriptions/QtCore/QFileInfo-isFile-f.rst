.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 681445a0f54188099b922f548a1466aa

Returns ``true`` if this object points to a file or to a symbolic link to a file. Returns ``false`` if the object points to something which isn't a file, such as a directory.

If the file is a symlink, this function returns true if the target is a regular file (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isBundle`.
