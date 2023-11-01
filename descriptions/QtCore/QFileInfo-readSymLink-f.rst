.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 9bd45816cdb034957a08feb2e4cf256d

Read the path the symlink references.

Returns the raw path referenced by the symbolic link, without resolving a relative path relative to the directory containing the symbolic link. The returned string will only be an absolute path if the symbolic link actually references it as such. Returns an empty string if the object is not a symbolic link.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`, :sip:ref:`~PyQt6.QtCore.QFileInfo.exists`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`.
