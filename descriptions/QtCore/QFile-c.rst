.. sip:class-description::
    :status: todo
    :brief: Interface for reading from and writing to files
    :digest: d8a77be8fe6fcd07f898b55423153060

The :sip:ref:`~PyQt6.QtCore.QFile` class provides an interface for reading from and writing to files.

:sip:ref:`~PyQt6.QtCore.QFile` is an I/O device for reading and writing text and binary files and `resources <https://doc.qt.io/qt-6/resources.html>`_. A :sip:ref:`~PyQt6.QtCore.QFile` may be used by itself or, more conveniently, with a :sip:ref:`~PyQt6.QtCore.QTextStream` or :sip:ref:`~PyQt6.QtCore.QDataStream`.

The file name is usually passed in the constructor, but it can be set at any time using :sip:ref:`~PyQt6.QtCore.QFile.setFileName`. :sip:ref:`~PyQt6.QtCore.QFile` expects the file separator to be '/' regardless of operating system. The use of other separators (e.g., '\\') is not supported.

You can check for a file's existence using :sip:ref:`~PyQt6.QtCore.QFile.exists`, and remove a file using :sip:ref:`~PyQt6.QtCore.QFile.remove`. (More advanced file system related operations are provided by :sip:ref:`~PyQt6.QtCore.QFileInfo` and :sip:ref:`~PyQt6.QtCore.QDir`.)

The file is opened with :sip:ref:`~PyQt6.QtCore.QFile.open`, closed with close(), and flushed with flush(). Data is usually read and written using :sip:ref:`~PyQt6.QtCore.QDataStream` or :sip:ref:`~PyQt6.QtCore.QTextStream`, but you can also call the :sip:ref:`~PyQt6.QtCore.QIODevice`-inherited functions read(), readLine(), readAll(), write(). :sip:ref:`~PyQt6.QtCore.QFile` also inherits getChar(), putChar(), and ungetChar(), which work one character at a time.

The size of the file is returned by :sip:ref:`~PyQt6.QtCore.QFile.size`. You can get the current file position using pos(), or move to a new file position using seek(). If you've reached the end of the file, atEnd() returns ``true``.

.. _qfile-reading-files-directly:

Reading Files Directly
----------------------

The following example reads a text file line by line:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-file-file.py
    :lines: 67-74

The :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.Text` flag passed to :sip:ref:`~PyQt6.QtCore.QFile.open` tells Qt to convert Windows-style line terminators ("\\r\\n") into C++-style terminators ("\\n"). By default, :sip:ref:`~PyQt6.QtCore.QFile` assumes binary, i.e. it doesn't perform any conversion on the bytes stored in the file.

.. _qfile-using-streams-to-read-files:

Using Streams to Read Files
---------------------------

The next example uses :sip:ref:`~PyQt6.QtCore.QTextStream` to read a text file line by line:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-file-file.py
    :lines: 81-89

:sip:ref:`~PyQt6.QtCore.QTextStream` takes care of converting the 8-bit data stored on disk into a 16-bit Unicode QString. By default, it assumes that the file is encoded in UTF-8. This can be changed using :sip:ref:`~PyQt6.QtCore.QTextStream.setEncoding`.

To write text, we can use operator<<(), which is overloaded to take a :sip:ref:`~PyQt6.QtCore.QTextStream` on the left and various data types (including QString) on the right:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-file-file.py
    :lines: 96-101

:sip:ref:`~PyQt6.QtCore.QDataStream` is similar, in that you can use operator<<() to write data and operator>>() to read it back. See the class documentation for details.

.. _qfile-signals:

Signals
-------

Unlike other :sip:ref:`~PyQt6.QtCore.QIODevice` implementations, such as :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, :sip:ref:`~PyQt6.QtCore.QFile` does not emit the aboutToClose(), bytesWritten(), or readyRead() signals. This implementation detail means that :sip:ref:`~PyQt6.QtCore.QFile` is not suitable for reading and writing certain types of files, such as device files on Unix platforms.

.. _qfile-platform-specific-issues:

Platform Specific Issues
------------------------

`Qt APIs related to I/O <https://doc.qt.io/qt-6/io.html>`_ use UTF-16 based QStrings to represent file paths. Standard C++ APIs (``<cstdio>`` or ``<iostream>``) or platform-specific APIs however often need a 8-bit encoded path. You can use :sip:ref:`~PyQt6.QtCore.QFile.encodeName` and :sip:ref:`~PyQt6.QtCore.QFile.decodeName` to convert between both representations.

On Unix, there are some special system files (e.g. in ``/proc``) for which :sip:ref:`~PyQt6.QtCore.QFile.size` will always return 0, yet you may still be able to read more data from such a file; the data is generated in direct response to you calling read(). In this case, however, you cannot use atEnd() to determine if there is more data to read (since atEnd() will return true for a file that claims to have size 0). Instead, you should either call readAll(), or call read() or readLine() repeatedly until no more data can be read. The next example uses :sip:ref:`~PyQt6.QtCore.QTextStream` to read ``/proc/modules`` line by line:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-file-file.py
    :lines: 118-127

File permissions are handled differently on Unix-like systems and Windows. In a non :sip:ref:`~PyQt6.QtCore.QIODevice.isWritable` directory on Unix-like systems, files cannot be created. This is not always the case on Windows, where, for instance, the 'My Documents' directory usually is not writable, but it is still possible to create files in it.

Qt's understanding of file permissions is limited, which affects especially the :sip:ref:`~PyQt6.QtCore.QFile.setPermissions` function. On Windows, Qt will set only the legacy read-only flag, and that only when none of the Write\* flags are passed. Qt does not manipulate access control lists (ACLs), which makes this function mostly useless for NTFS volumes. It may still be of use for USB sticks that use VFAT file systems. POSIX ACLs are not manipulated, either.

On Android, some limitations apply when dealing with `content URIs <https://doc.qt.io/qt-6/https://developer.android.com/guide/topics/providers/content-provider-basics#ContentURIs>`_:

* Access permissions might be needed by prompting the user through the :sip:ref:`~PyQt6.QtWidgets.QFileDialog` which implements `Android's native file picker <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage/shared/documents-files>`_.

* Aim to follow the `Scoped storage <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage#scoped-storage>`_ guidelines, such as using app specific directories instead of other public external directories. For more information, also see `storage best practices <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage/use-cases>`_.

* Due to the design of Qt APIs (e.g. :sip:ref:`~PyQt6.QtCore.QFile`), it's not possible to fully integrate the latter APIs with Android's `MediaStore <https://doc.qt.io/qt-6/https://developer.android.com/reference/android/provider/MediaStore>`_ APIs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream`, :sip:ref:`~PyQt6.QtCore.QDataStream`, :sip:ref:`~PyQt6.QtCore.QFileInfo`, :sip:ref:`~PyQt6.QtCore.QDir`, `The Qt Resource System <https://doc.qt.io/qt-6/resources.html>`_.
