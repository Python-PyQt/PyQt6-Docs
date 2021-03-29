.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 5b86990892072d7d61b417b055c17190

Returns ``true`` if this object points to a bundle or to a symbolic link to a bundle on macOS and iOS; otherwise returns ``false``.

If the file is a symlink, this function returns true if the target is a bundle (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`.
