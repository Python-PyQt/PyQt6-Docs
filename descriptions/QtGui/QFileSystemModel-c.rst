.. sip:class-description::
    :status: todo
    :brief: Data model for the local filesystem
    :digest: b56c1966f3d04b9510da992f85512861

The :sip:ref:`~PyQt6.QtGui.QFileSystemModel` class provides a data model for the local filesystem.

This class provides access to the local filesystem, providing functions for renaming and removing files and directories, and for creating new directories. In the simplest case, it can be used with a suitable display widget as part of a browser or filter.

:sip:ref:`~PyQt6.QtGui.QFileSystemModel` can be accessed using the standard interface provided by :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, but it also provides some convenience functions that are specific to a directory model. The :sip:ref:`~PyQt6.QtGui.QFileSystemModel.fileInfo`, :sip:ref:`~PyQt6.QtGui.QFileSystemModel.isDir`, :sip:ref:`~PyQt6.QtGui.QFileSystemModel.fileName` and :sip:ref:`~PyQt6.QtGui.QFileSystemModel.filePath` functions provide information about the underlying files and directories related to items in the model. Directories can be created and removed using :sip:ref:`~PyQt6.QtGui.QFileSystemModel.mkdir`, :sip:ref:`~PyQt6.QtGui.QFileSystemModel.rmdir`.

.. _qfilesystemmodel-example-usage:

Example Usage
-------------

A directory model that displays the contents of a default directory is usually constructed with a parent object:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-shareddirmodel-main.py
    :lines: 69-70

A tree view can be used to display the contents of the model

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-shareddirmodel-main.py
    :lines: 72-74

and the contents of a particular directory can be displayed by setting the tree view's root index:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-shareddirmodel-main.py
    :lines: 76-76

The view's root index can be used to control how much of a hierarchical model is displayed. :sip:ref:`~PyQt6.QtGui.QFileSystemModel` provides a convenience function that returns a suitable model index for a path to a directory within the model.

.. _qfilesystemmodel-caching-and-performance:

Caching and Performance
-----------------------

:sip:ref:`~PyQt6.QtGui.QFileSystemModel` uses a separate thread to populate itself, so it will not cause the main thread to hang as the file system is being queried. Calls to :sip:ref:`~PyQt6.QtGui.QFileSystemModel.rowCount` will return ``0`` until the model populates a directory. The thread in which the :sip:ref:`~PyQt6.QtGui.QFileSystemModel` lives needs to run an event loop to process the incoming data.

:sip:ref:`~PyQt6.QtGui.QFileSystemModel` will not start populating itself until :sip:ref:`~PyQt6.QtGui.QFileSystemModel.setRootPath` is called. This prevents any unnecessary querying of the system's root file system, such as enumerating the drives on Windows, until that point.

:sip:ref:`~PyQt6.QtGui.QFileSystemModel` keeps a cache with file information. The cache is automatically kept up to date using the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher`.

.. seealso:: `Model Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-classes>`_.
