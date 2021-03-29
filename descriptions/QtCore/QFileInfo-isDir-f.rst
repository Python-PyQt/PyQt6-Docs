.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 414e887748f5f01f99cd008b929b5f50

Returns ``true`` if this object points to a directory or to a symbolic link to a directory; otherwise returns ``false``.

If the file is a symlink, this function returns true if the target is a directory (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isBundle`.
