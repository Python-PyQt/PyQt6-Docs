.. sip:class-description::
    :status: todo
    :brief: Provides a dialog that allows users to select files or directories
    :digest: 95d58991bb1d786cfcf9adb8ccdc2c27

Provides a dialog that allows users to select files or directories.

The :sip:ref:`~PyQt6.QtWidgets.QFileDialog` class enables users to browse the file system and select one or more files or directories.

.. image:: ../../../images/qfiledialog.png

:sip:ref:`~PyQt6.QtWidgets.QFileDialog` is commonly used to prompt users to open or save files, or to select directories. The easiest way to use :sip:ref:`~PyQt6.QtWidgets.QFileDialog` is through its static convenience functions, such as :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileName`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 54-55

In this example, a modal :sip:ref:`~PyQt6.QtWidgets.QFileDialog` is created using a static function. The dialog initially displays the contents of the ``/home/jana`` directory and shows files matching the patterns in ``"Image Files (\*.png \*.jpg \*.bmp)"``. The window title is set to ``Open Image``.

.. _qfiledialog-file-filters:

File filters
------------

.. _qfiledialog-filtering-files-by-name-or-extension:

Filtering files by name or extension
....................................

To filter the displayed files by name or extension, use the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setNameFilter` or :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setNameFilters` functions. Multiple filters can be specified by separating them with two semicolons (;;):

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 60-60

.. _qfiledialog-filtering-files-by-mime-type:

Filtering files by MIME type
............................

To filter the displayed files by MIME type, use the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setMimeTypeFilters` function:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 135-142

.. _qfiledialog-file-filter-case-sensitivity:

File filter case sensitivity
............................

Depending on target platform, file filters can be case-sensitive or case-insensitive.

.. _qfiledialog-file-modes:

File modes
----------

:sip:ref:`~PyQt6.QtWidgets.QFileDialog` supports several file modes, which determine what the user can select:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 65-66

* **AnyFile**: The user can select any file, including files that do not exist (useful for ``Save As`` dialogs).

* **ExistingFile**: The user must select an existing file.

* **Directory**: The user can select a directory.

See the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.FileMode` enum for the complete list of modes.

The :sip:ref:`~PyQt6.QtWidgets.QFileDialog.fileMode` property contains the current mode of operation. Use :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setFileMode` to change it.

.. _qfiledialog-view-modes:

View modes
----------

:sip:ref:`~PyQt6.QtWidgets.QFileDialog` provides two view modes:

* **List**: Displays files and directories as a simple list.

* **Detail**: Displays additional information such as file size and modification date.

Set the view mode with :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setViewMode`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 76-76

.. _qfiledialog-retrieving-selected-files:

Retrieving selected files
-------------------------

After the dialog is accepted, use :sip:ref:`~PyQt6.QtWidgets.QFileDialog.selectedFiles` to retrieve the user's selection:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 81-83

The dialog's working directory can be set with :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setDirectory`. You can pre-select a file using :sip:ref:`~PyQt6.QtWidgets.QFileDialog.selectFile`.

.. _qfiledialog-platform-notes:

Platform notes
--------------

By default, :sip:ref:`~PyQt6.QtWidgets.QFileDialog` uses the platform's native file dialog if available. In this case, some widget-specific APIs (such as layout() and :sip:ref:`~PyQt6.QtWidgets.QFileDialog.itemDelegate`) may return ``null``. Also, not all platforms display file dialogs with a title bar, so the caption text may not be visible.

To force the use of the Qt widget-based dialog, set the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.DontUseNativeDialog` option or the :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DontUseNativeDialogs` application attribute.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo`, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtWidgets.QColorDialog`, :sip:ref:`~PyQt6.QtWidgets.QFontDialog`, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
