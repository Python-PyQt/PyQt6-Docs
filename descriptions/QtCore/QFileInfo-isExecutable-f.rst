.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: fcfae264ee629ca88ea1ebc5c610aa56

Returns ``true`` if the file is executable; otherwise returns ``false``.

If the file is a symlink, this function returns true if the target is executable (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isReadable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isWritable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.permission`.
