.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: aa7955cbba658013b65edde95f751cba

Returns ``true`` if the file path can be used directly with native APIs. Returns ``false`` if the file is otherwise supported by a virtual file system inside Qt, such as `the Qt Resource System <https://doc.qt.io/qt-6/resources.html>`_.

**Note:** Native paths may still require conversion of path separators and character encoding, depending on platform and input requirements of the native API.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.toNativeSeparators`, :sip:ref:`~PyQt6.QtCore.QFile.encodeName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalFilePath`.
