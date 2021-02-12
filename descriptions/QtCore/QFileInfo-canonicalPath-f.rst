.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 9ca2871ee90db662d54d104b57f2e397

Returns the file's path canonical path (excluding the file name), i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the file does not exist,  returns an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.path`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absolutePath`.
