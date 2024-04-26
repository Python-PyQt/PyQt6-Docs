.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 832999a1d3ec58527383ba1c89a18888

Returns ``true`` if this object points to a file or to a symbolic link to a file. Returns ``false`` if the object points to something that is not a file (such as a directory) or that does not exist.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isBundle`.
