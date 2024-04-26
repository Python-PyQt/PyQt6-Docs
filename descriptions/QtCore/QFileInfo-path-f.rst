.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: c112652a4d3fc343dd511997cc33f9d0

Returns the path of the file system entry this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to, excluding the entry's name.

**Note:** If this :sip:ref:`~PyQt6.QtCore.QFileInfo` is given a path ending with a directory separator ``'/'``, the entry's name part is considered empty. In this case, this function will return the entire path.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absolutePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalPath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.dir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
