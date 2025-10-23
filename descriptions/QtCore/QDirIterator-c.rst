.. sip:class-description::
    :status: todo
    :brief: Iterator for directory entrylists
    :digest: 121c23d20f2db923e2d313bf26188ad5

The :sip:ref:`~PyQt6.QtCore.QDirIterator` class provides an iterator for directory entrylists.

You can use :sip:ref:`~PyQt6.QtCore.QDirIterator` to navigate entries of a directory one at a time. It is similar to :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`, but because it lists entries one at a time instead of all at once, it scales better and is more suitable for large directories. It also supports listing directory contents recursively, and following symbolic links. Unlike :sip:ref:`~PyQt6.QtCore.QDir.entryList`, :sip:ref:`~PyQt6.QtCore.QDirIterator` does not support sorting.

The :sip:ref:`~PyQt6.QtCore.QDirIterator` constructor takes a :sip:ref:`~PyQt6.QtCore.QDir` or a directory as argument. After construction, the iterator is located before the first directory entry. Here's how to iterate over all the entries sequentially:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdiriterator.py
    :lines: 54-63

Here's how to find and read all files filtered by name, recursively:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdiriterator.py
    :lines: 67-72

The :sip:ref:`~PyQt6.QtCore.QDirIterator.next` and :sip:ref:`~PyQt6.QtCore.QDirIterator.nextFileInfo` functions advance the iterator and return the path or the :sip:ref:`~PyQt6.QtCore.QFileInfo` of the next directory entry. You can also call :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath` or :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo` to get the current file path or :sip:ref:`~PyQt6.QtCore.QFileInfo` without first advancing the iterator. The :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName` function returns only the name of the file, similar to how :sip:ref:`~PyQt6.QtCore.QDir.entryList` works.

Unlike Qt's container iterators, :sip:ref:`~PyQt6.QtCore.QDirIterator` is uni-directional (i.e., you cannot iterate directories in reverse order) and does not allow random access.

**Note:** This class is deprecated and may be removed in a Qt release. Use QDirListing instead, see `Porting QDirIterator to QDirListing <https://doc.qt.io/qt-6/qdiriterator-to-qdirlisting-porting.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QDir.entryList`.
