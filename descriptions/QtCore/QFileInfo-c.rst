.. sip:class-description::
    :status: todo
    :brief: OS-independent API to retrieve information about file system entries
    :digest: a28e8c60591ff3f99cf6c7a0d0a9bfe1

The :sip:ref:`~PyQt6.QtCore.QFileInfo` class provides an OS-independent API to retrieve information about file system entries.

:sip:ref:`~PyQt6.QtCore.QFileInfo` provides information about a file system entry, such as its name, path, access rights and whether it is a regular file, directory or symbolic link. The entry's size and last modified/read times are also available. :sip:ref:`~PyQt6.QtCore.QFileInfo` can also be used to obtain information about a Qt `resource <https://doc.qt.io/qt-6/resources.html>`_.

A :sip:ref:`~PyQt6.QtCore.QFileInfo` can point to a file system entry with either an absolute or a relative path:

* On Unix, absolute paths begin with the directory separator ``'/'``. On Windows, absolute paths begin with a drive specification (for example, ``D:/``).

* Relative paths begin with a directory name or a regular file name and specify a file system entry's path relative to the current working directory.

An example of an absolute path is the string ``"/tmp/quartz"``. A relative path may look like ``"src/fatlib"``. You can use the function :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative` to check whether a :sip:ref:`~PyQt6.QtCore.QFileInfo` is using a relative or an absolute path. You can call the function :sip:ref:`~PyQt6.QtCore.QFileInfo.makeAbsolute` to convert a relative :sip:ref:`~PyQt6.QtCore.QFileInfo`'s path to an absolute path.

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

The file system entry path that the :sip:ref:`~PyQt6.QtCore.QFileInfo` works on is set in the constructor or later with :sip:ref:`~PyQt6.QtCore.QFileInfo.setFile`. Use :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` to see if the entry actually exists and :sip:ref:`~PyQt6.QtCore.QFileInfo.size` to get its size.

The file system entry's type is obtained with :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, and :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`. The :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget` function provides the absolute path of the target the symlink points to.

The path elements of the file system entry can be extracted with :sip:ref:`~PyQt6.QtCore.QFileInfo.path` and :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`. The :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`'s parts can be extracted with :sip:ref:`~PyQt6.QtCore.QFileInfo.baseName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.suffix`, or :sip:ref:`~PyQt6.QtCore.QFileInfo.completeSuffix`. :sip:ref:`~PyQt6.QtCore.QFileInfo` objects referring to directories created by Qt classes will not have a trailing directory separator ``'/'``. If you wish to use trailing separators in your own file info objects, just append one to the entry's path given to the constructors or :sip:ref:`~PyQt6.QtCore.QFileInfo.setFile`.

Date and time related information are returned by :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, and :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`. Information about access permissions can be obtained with :sip:ref:`~PyQt6.QtCore.QFileInfo.isReadable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isWritable`, and :sip:ref:`~PyQt6.QtCore.QFileInfo.isExecutable`. Ownership information can be obtained with :sip:ref:`~PyQt6.QtCore.QFileInfo.owner`, :sip:ref:`~PyQt6.QtCore.QFileInfo.ownerId`, :sip:ref:`~PyQt6.QtCore.QFileInfo.group`, and :sip:ref:`~PyQt6.QtCore.QFileInfo.groupId`. You can also examine permissions and ownership in a single statement using the :sip:ref:`~PyQt6.QtCore.QFileInfo.permission` function.

.. _qfileinfo-symbolic-links-and-shortcuts:

Symbolic Links and Shortcuts
----------------------------

On Unix (including macOS and iOS), the property getter functions in this class return the properties such as times and size of the target, not the symlink, because Unix handles symlinks transparently. Opening a symlink using :sip:ref:`~PyQt6.QtCore.QFile` effectively opens the link's target. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 59-72

On Windows, shortcuts (``.lnk`` files) are currently treated as symlinks. As on Unix systems, the property getters return the size of the target, not the ``.lnk`` file itself. This behavior is deprecated and will likely be removed in a future version of Qt, after which ``.lnk`` files will be treated as regular files.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 77-90

.. _qfileinfo-ntfs-permissions:

NTFS permissions
----------------

On NTFS file systems, ownership and permissions checking is disabled by default for performance reasons. To enable it, include the following line:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 55-55

Permission checking is then turned on and off by incrementing and decrementing ``qt_ntfs_permission_lookup`` by 1.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 59-60

**Note:** Since this is a non-atomic global variable, it is only safe to increment or decrement ``qt_ntfs_permission_lookup`` before any threads other than the main thread have started or after every thread other than the main thread has ended.

**Note:** From Qt 6.6 the variable ``qt_ntfs_permission_lookup`` is deprecated. Please use the following alternatives.

The safe and easy way to manage permission checks is to use the RAII class ``QNtfsPermissionCheckGuard``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py

If you need more fine-grained control, it is possible to manage the permission with the following functions instead:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py

.. _qfileinfo-performance-considerations:

Performance Considerations
--------------------------

Some of :sip:ref:`~PyQt6.QtCore.QFileInfo`'s functions have to query the file system, but for performance reasons, some functions only operate on the path string. For example: To return the absolute path of a relative entry's path, :sip:ref:`~PyQt6.QtCore.QFileInfo.absolutePath` has to query the file system. The :sip:ref:`~PyQt6.QtCore.QFileInfo.path` function, however, can work on the file name directly, and so it is faster.

:sip:ref:`~PyQt6.QtCore.QFileInfo` also caches information about the file system entry it refers to. Because the file system can be changed by other users or programs, or even by other parts of the same program, there is a function that refreshes the information stored in :sip:ref:`~PyQt6.QtCore.QFileInfo`, namely :sip:ref:`~PyQt6.QtCore.QFileInfo.refresh`. To switch off a :sip:ref:`~PyQt6.QtCore.QFileInfo`'s caching (that is, force it to query the underlying file system every time you request information from it), call :sip:ref:`~PyQt6.QtCore.QFileInfo.setCaching`\ (false).

Fetching information from the file system is typically done by calling (possibly) expensive system functions, so :sip:ref:`~PyQt6.QtCore.QFileInfo` (depending on the implementation) might not fetch all the information from the file system at construction. To make sure that all information is read from the file system immediately, use the :sip:ref:`~PyQt6.QtCore.QFileInfo.stat` member function.

:sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, and :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime` return times in *local time* by default. Since native file system API typically uses UTC, this requires a conversion. If you don't actually need the local time, you can avoid this by requesting the time in :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` directly.

.. _qfileinfo-platform-specific-issues:

Platform Specific Issues
------------------------

On Android, some limitations apply when dealing with `content URIs <https://doc.qt.io/qt-6/https://developer.android.com/guide/topics/providers/content-provider-basics#ContentURIs>`_:

* Access permissions might be needed by prompting the user through the :sip:ref:`~PyQt6.QtWidgets.QFileDialog` which implements `Android's native file picker <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage/shared/documents-files>`_.

* Aim to follow the `Scoped storage <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage#scoped-storage>`_ guidelines, such as using app specific directories instead of other public external directories. For more information, also see `storage best practices <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage/use-cases>`_.

* Due to the design of Qt APIs (e.g. :sip:ref:`~PyQt6.QtCore.QFile`), it's not possible to fully integrate the latter APIs with Android's `MediaStore <https://doc.qt.io/qt-6/https://developer.android.com/reference/android/provider/MediaStore>`_ APIs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QFile`.
