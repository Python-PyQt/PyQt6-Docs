.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 65ca0594d27fc7de086d3ab88d466959

Returns ``true`` if this object points to an alias; otherwise returns ``false``.

Aliases only exist on macOS. They are treated as regular files, so opening an alias will open the file itself. In order to open the file or directory an alias references use :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.

**Note:** Even if an alias points to a non existing file, isAlias() returns true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.
