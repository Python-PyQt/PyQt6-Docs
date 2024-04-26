.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 2b1fa27004e7b52a7cebfaeb6f2ba693

Returns the file system entry's canonical path (excluding the entry's name), i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the entry does not exist, this method returns an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.path`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absolutePath`.
