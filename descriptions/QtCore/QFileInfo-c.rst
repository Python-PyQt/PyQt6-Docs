.. sip:class-description::
    :status: todo
    :brief: System-independent file information
    :digest: d9b382f51aba1310f756ba3e298a1aba

The :sip:ref:`~PyQt6.QtCore.QFileInfo` class provides system-independent file information.

:sip:ref:`~PyQt6.QtCore.QFileInfo` provides information about a file's name and position (path) in the file system, its access rights and whether it is a directory or symbolic link, etc. The file's size and last modified/read times are also available. :sip:ref:`~PyQt6.QtCore.QFileInfo` can also be used to obtain information about a Qt `resource <https://doc.qt.io/qt-6/resources.html>`_.

A :sip:ref:`~PyQt6.QtCore.QFileInfo` can point to a file with either a relative or an absolute file path. Absolute file paths begin with the directory separator "/" (or with a drive specification on Windows). Relative file names begin with a directory name or a file name and specify a path relative to the current working directory. An example of an absolute path is the string "/tmp/quartz". A relative path might look like "src/fatlib". You can use the function :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative` to check whether a :sip:ref:`~PyQt6.QtCore.QFileInfo` is using a relative or an absolute file path. You can call the function :sip:ref:`~PyQt6.QtCore.QFileInfo.makeAbsolute` to convert a relative :sip:ref:`~PyQt6.QtCore.QFileInfo`'s path to an absolute path.

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

The file that the :sip:ref:`~PyQt6.QtCore.QFileInfo` works on is set in the constructor or later with :sip:ref:`~PyQt6.QtCore.QFileInfo.setFile`. Use :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` to see if the file exists and :sip:ref:`~PyQt6.QtCore.QFileInfo.size` to get its size.

The file's type is obtained with :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir` and :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`. The :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget` function provides the name of the file the symlink points to.

On Unix (including macOS and iOS), the property getter functions in this class return the properties such as times and size of the target file, not the symlink, because Unix handles symlinks transparently. Opening a symlink using :sip:ref:`~PyQt6.QtCore.QFile` effectively opens the link's target. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 59-72

On Windows, shortcuts (``.lnk`` files) are currently treated as symlinks. As on Unix systems, the property getters return the size of the targeted file, not the ``.lnk`` file itself. This behavior is deprecated and will likely be removed in a future version of Qt, after which ``.lnk`` files will be treated as regular files.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 77-90

Elements of the file's name can be extracted with :sip:ref:`~PyQt6.QtCore.QFileInfo.path` and :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`. The :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`'s parts can be extracted with :sip:ref:`~PyQt6.QtCore.QFileInfo.baseName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.suffix` or :sip:ref:`~PyQt6.QtCore.QFileInfo.completeSuffix`. :sip:ref:`~PyQt6.QtCore.QFileInfo` objects to directories created by Qt classes will not have a trailing file separator. If you wish to use trailing separators in your own file info objects, just append one to the file name given to the constructors or :sip:ref:`~PyQt6.QtCore.QFileInfo.setFile`.

The file's dates are returned by :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead` and :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`. Information about the file's access permissions is obtained with :sip:ref:`~PyQt6.QtCore.QFileInfo.isReadable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isWritable` and :sip:ref:`~PyQt6.QtCore.QFileInfo.isExecutable`. The file's ownership is available from :sip:ref:`~PyQt6.QtCore.QFileInfo.owner`, :sip:ref:`~PyQt6.QtCore.QFileInfo.ownerId`, :sip:ref:`~PyQt6.QtCore.QFileInfo.group` and :sip:ref:`~PyQt6.QtCore.QFileInfo.groupId`. You can examine a file's permissions and ownership in a single statement using the :sip:ref:`~PyQt6.QtCore.QFileInfo.permission` function.

.. _qfileinfo-ntfs-permissions:

**Note:** On NTFS file systems, ownership and permissions checking is disabled by default for performance reasons. To enable it, include the following line:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 55-55

Permission checking is then turned on and off by incrementing and decrementing ``qt_ntfs_permission_lookup`` by 1.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 59-60

**Note:** Since this is a non-atomic global variable, it is only safe to increment or decrement ``qt_ntfs_permission_lookup`` before any threads other than the main thread have started or after every thread other than the main thread has ended.

.. _qfileinfo-performance-issues:

Performance Issues
------------------

Some of :sip:ref:`~PyQt6.QtCore.QFileInfo`'s functions query the file system, but for performance reasons, some functions only operate on the file name itself. For example: To return the absolute path of a relative file name, :sip:ref:`~PyQt6.QtCore.QFileInfo.absolutePath` has to query the file system. The :sip:ref:`~PyQt6.QtCore.QFileInfo.path` function, however, can work on the file name directly, and so it is faster.

**Note:** To speed up performance, :sip:ref:`~PyQt6.QtCore.QFileInfo` caches information about the file.

Because files can be changed by other users or programs, or even by other parts of the same program, there is a function that refreshes the file information: :sip:ref:`~PyQt6.QtCore.QFileInfo.refresh`. If you want to switch off a :sip:ref:`~PyQt6.QtCore.QFileInfo`'s caching and force it to access the file system every time you request information from it call :sip:ref:`~PyQt6.QtCore.QFileInfo.setCaching`\ (false). If you want to make sure that all information is read from the file system, use :sip:ref:`~PyQt6.QtCore.QFileInfo.stat`.

.. _qfileinfo-platform-specific-issues:

Platform Specific Issues
------------------------

On Android, some limitations apply when dealing with `content URIs <https://doc.qt.io/qt-6/https://developer.android.com/guide/topics/providers/content-provider-basics#ContentURIs>`_:

* Access permissions might be needed by prompting the user through the :sip:ref:`~PyQt6.QtWidgets.QFileDialog` which implements Android's native file picker.

* Aim to follow the `Scoped storage <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage#scoped-storage>`_ guidelines, such as using app specific directories instead of other public external directories. For more information, also see `storage best practices <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage/use-cases>`_.

* Due to the design of Qt APIs (e.g. :sip:ref:`~PyQt6.QtCore.QFile`), it's not possible to fully integrate the latter APIs with Android's `MediaStore <https://doc.qt.io/qt-6/https://developer.android.com/reference/android/provider/MediaStore>`_ APIs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QFile`.
