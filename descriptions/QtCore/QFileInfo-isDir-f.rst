.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: fc6e26fec62d069f75bbbf1844fc0a6c

Returns ``true`` if this object points to a directory or to a symbolic link to a directory. Returns ``false`` if the object points to something that is not a directory (such as a file) or that does not exist.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isBundle`.
