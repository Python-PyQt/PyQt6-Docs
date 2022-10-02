.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 8eea26731553e31ed29d2eb3c9f6fde7

Returns the file's path canonical path (excluding the file name), i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the file does not exist, canonicalPath() returns an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.path`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absolutePath`.
