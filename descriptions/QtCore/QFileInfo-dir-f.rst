.. sip:method-description::
    :status: todo
    :pysig: 57ae641f7e7f9a6c1de44f36ce2eb561
    :realsig: () const
    :digest: bc173bfcd1fa45ec5cfb92e2b74dd578

Returns the path of the object's parent directory as a :sip:ref:`~PyQt6.QtCore.QDir` object.

**Note:** The :sip:ref:`~PyQt6.QtCore.QDir` returned always corresponds to the object's parent directory, even if the :sip:ref:`~PyQt6.QtCore.QFileInfo` represents a directory.

For each of the following, dir() returns the :sip:ref:`~PyQt6.QtCore.QDir` ``"~/examples/191697"``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-fileinfo-main.py
    :lines: 66-68

For each of the following, dir() returns the :sip:ref:`~PyQt6.QtCore.QDir` ``"."``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-fileinfo-main.py
    :lines: 71-73

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.absolutePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absoluteDir`.
