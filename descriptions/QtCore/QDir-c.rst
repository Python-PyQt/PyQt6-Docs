.. sip:class-description::
    :status: todo
    :brief: Access to directory structures and their contents
    :digest: 3f321b70554eede1919a04863910cf38

The :sip:ref:`~PyQt6.QtCore.QDir` class provides access to directory structures and their contents.

A :sip:ref:`~PyQt6.QtCore.QDir` is used to manipulate path names, access information regarding paths and files, and manipulate the underlying file system. It can also be used to access Qt's `resource system <https://doc.qt.io/qt-6/resources.html>`_.

Qt uses "/" as a universal directory separator in the same way that "/" is used as a path separator in URLs. If you always use "/" as a directory separator, Qt will translate your paths to conform to the underlying operating system.

A :sip:ref:`~PyQt6.QtCore.QDir` can point to a file using either a relative or an absolute path. Absolute paths begin with the directory separator (optionally preceded by a drive specification under Windows). Relative file names begin with a directory name or a file name and specify a path relative to the current directory.

Examples of absolute paths:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 58-59

On Windows, the second example above will be translated to ``C:\Users`` when used to access files.

Examples of relative paths:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 64-64

You can use the :sip:ref:`~PyQt6.QtCore.QDir.isRelative` or :sip:ref:`~PyQt6.QtCore.QDir.isAbsolute` functions to check if a :sip:ref:`~PyQt6.QtCore.QDir` is using a relative or an absolute file path. Call :sip:ref:`~PyQt6.QtCore.QDir.makeAbsolute` to convert a relative :sip:ref:`~PyQt6.QtCore.QDir` to an absolute one.

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

.. _qdir-navigation-and-directory-operations:

Navigation and Directory Operations
-----------------------------------

A directory's path can be obtained with the :sip:ref:`~PyQt6.QtCore.QDir.path` function, and a new path set with the :sip:ref:`~PyQt6.QtCore.QDir.setPath` function. The absolute path to a directory is found by calling :sip:ref:`~PyQt6.QtCore.QDir.absolutePath`.

The name of a directory is found using the :sip:ref:`~PyQt6.QtCore.QDir.dirName` function. This typically returns the last element in the absolute path that specifies the location of the directory. However, it can also return "." if the :sip:ref:`~PyQt6.QtCore.QDir` represents the current directory.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 69-70

The path for a directory can also be changed with the :sip:ref:`~PyQt6.QtCore.QDir.cd` and :sip:ref:`~PyQt6.QtCore.QDir.cdUp` functions, both of which operate like familiar shell commands. When :sip:ref:`~PyQt6.QtCore.QDir.cd` is called with the name of an existing directory, the :sip:ref:`~PyQt6.QtCore.QDir` object changes directory so that it represents that directory instead. The :sip:ref:`~PyQt6.QtCore.QDir.cdUp` function changes the directory of the :sip:ref:`~PyQt6.QtCore.QDir` object so that it refers to its parent directory; i.e. cd("..") is equivalent to :sip:ref:`~PyQt6.QtCore.QDir.cdUp`.

Directories can be created with :sip:ref:`~PyQt6.QtCore.QDir.mkdir`, renamed with :sip:ref:`~PyQt6.QtCore.QDir.rename`, and removed with :sip:ref:`~PyQt6.QtCore.QDir.rmdir`.

You can test for the presence of a directory with a given name by using :sip:ref:`~PyQt6.QtCore.QDir.exists`, and the properties of a directory can be tested with :sip:ref:`~PyQt6.QtCore.QDir.isReadable`, :sip:ref:`~PyQt6.QtCore.QDir.isAbsolute`, :sip:ref:`~PyQt6.QtCore.QDir.isRelative`, and :sip:ref:`~PyQt6.QtCore.QDir.isRoot`.

The :sip:ref:`~PyQt6.QtCore.QDir.refresh` function re-reads the directory's data from disk.

.. _qdir-files-and-directory-contents:

Files and Directory Contents
----------------------------

Directories contain a number of entries, representing files, directories, and symbolic links. The number of entries in a directory is returned by :sip:ref:`~PyQt6.QtCore.QDir.count`. A string list of the names of all the entries in a directory can be obtained with :sip:ref:`~PyQt6.QtCore.QDir.entryList`. If you need information about each entry, use :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList` to obtain a list of :sip:ref:`~PyQt6.QtCore.QFileInfo` objects.

Paths to files and directories within a directory can be constructed using :sip:ref:`~PyQt6.QtCore.QDir.filePath` and :sip:ref:`~PyQt6.QtCore.QDir.absoluteFilePath`. The :sip:ref:`~PyQt6.QtCore.QDir.filePath` function returns a path to the specified file or directory relative to the path of the :sip:ref:`~PyQt6.QtCore.QDir` object; :sip:ref:`~PyQt6.QtCore.QDir.absoluteFilePath` returns an absolute path to the specified file or directory. Neither of these functions checks for the existence of files or directory; they only construct paths.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 75-77

Files can be removed by using the :sip:ref:`~PyQt6.QtCore.QDir.remove` function. Directories cannot be removed in the same way as files; use :sip:ref:`~PyQt6.QtCore.QDir.rmdir` to remove them instead.

It is possible to reduce the number of entries returned by :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList` by applying filters to a :sip:ref:`~PyQt6.QtCore.QDir` object. You can apply a name filter to specify a pattern with wildcards that file names need to match, an attribute filter that selects properties of entries and can distinguish between files and directories, and a sort order.

Name filters are lists of strings that are passed to :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters`. Attribute filters consist of a bitwise OR combination of Filters, and these are specified when calling :sip:ref:`~PyQt6.QtCore.QDir.setFilter`. The sort order is specified using :sip:ref:`~PyQt6.QtCore.QDir.setSorting` with a bitwise OR combination of SortFlags.

You can test to see if a filename matches a filter using the :sip:ref:`~PyQt6.QtCore.QDir.match` function.

Filter and sort order flags may also be specified when calling :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList` in order to override previously defined behavior.

.. _qdir-the-current-directory-and-other-special-paths:

The Current Directory and Other Special Paths
---------------------------------------------

Access to some common directories is provided with a number of static functions that return :sip:ref:`~PyQt6.QtCore.QDir` objects. There are also corresponding functions for these that return strings:

+---------------------------------------+-------------------------------------------+-------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QDir`         | QString                                   | Return Value                        |
+=======================================+===========================================+=====================================+
| :sip:ref:`~PyQt6.QtCore.QDir.current` | :sip:ref:`~PyQt6.QtCore.QDir.currentPath` | The application's working directory |
+---------------------------------------+-------------------------------------------+-------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QDir.home`    | :sip:ref:`~PyQt6.QtCore.QDir.homePath`    | The user's home directory           |
+---------------------------------------+-------------------------------------------+-------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QDir.root`    | :sip:ref:`~PyQt6.QtCore.QDir.rootPath`    | The root directory                  |
+---------------------------------------+-------------------------------------------+-------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QDir.temp`    | :sip:ref:`~PyQt6.QtCore.QDir.tempPath`    | The system's temporary directory    |
+---------------------------------------+-------------------------------------------+-------------------------------------+

The :sip:ref:`~PyQt6.QtCore.QDir.setCurrent` static function can also be used to set the application's working directory.

If you want to find the directory containing the application's executable, see :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationDirPath`.

The :sip:ref:`~PyQt6.QtCore.QDir.drives` static function provides a list of root directories for each device that contains a filing system. On Unix systems this returns a list containing a single root directory "/"; on Windows the list will usually contain ``C:/``, and possibly other drive letters such as ``D:/``, depending on the configuration of the user's system.

.. _qdir-path-manipulation-and-strings:

Path Manipulation and Strings
-----------------------------

Paths containing "." elements that reference the current directory at that point in the path, ".." elements that reference the parent directory, and symbolic links can be reduced to a canonical form using the :sip:ref:`~PyQt6.QtCore.QDir.canonicalPath` function.

Paths can also be simplified by using :sip:ref:`~PyQt6.QtCore.QDir.cleanPath` to remove redundant "/" and ".." elements.

It is sometimes necessary to be able to show a path in the native representation for the user's platform. The static :sip:ref:`~PyQt6.QtCore.QDir.toNativeSeparators` function returns a copy of the specified path in which each directory separator is replaced by the appropriate separator for the underlying operating system.

.. _qdir-examples:

Examples
--------

Check if a directory exists:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 82-84

(We could also use one of the static convenience functions :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` or :sip:ref:`~PyQt6.QtCore.QFile.exists`.)

Traversing directories and reading a file:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdir.py
    :lines: 89-96

A program that lists all the files in the current directory (excluding symbolic links), sorted by size, smallest first:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qdir-listfiles-main.py
    :lines: 54-73

.. _qdir-platform-specific-issues:

Platform Specific Issues
------------------------

On Android, some limitations apply when dealing with `content URIs <https://doc.qt.io/qt-6/https://developer.android.com/guide/topics/providers/content-provider-basics#ContentURIs>`_:

* Access permissions might be needed by prompting the user through the :sip:ref:`~PyQt6.QtWidgets.QFileDialog` which implements `Android's native file picker <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage/shared/documents-files>`_.

* Aim to follow the `Scoped storage <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage#scoped-storage>`_ guidelines, such as using app specific directories instead of other public external directories. For more information, also see `storage best practices <https://doc.qt.io/qt-6/https://developer.android.com/training/data-storage/use-cases>`_.

* Due to the design of Qt APIs (e.g. :sip:ref:`~PyQt6.QtCore.QFile`), it's not possible to fully integrate the latter APIs with Android's `MediaStore <https://doc.qt.io/qt-6/https://developer.android.com/reference/android/provider/MediaStore>`_ APIs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo`, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationDirPath`, `Fetch More Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-fetchmore-example.html>`_.
