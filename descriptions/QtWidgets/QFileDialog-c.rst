.. sip:class-description::
    :status: todo
    :brief: Dialog that allows users to select files or directories
    :digest: 044429574e2bf8afcdc482721827d9d2

The :sip:ref:`~PyQt6.QtWidgets.QFileDialog` class provides a dialog that allows users to select files or directories.

The :sip:ref:`~PyQt6.QtWidgets.QFileDialog` class enables a user to traverse the file system to select one or many files or a directory.

.. image:: ../../../images/qtquickdialogs-filedialog-gtk.png

The easiest way to create a :sip:ref:`~PyQt6.QtWidgets.QFileDialog` is to use the static functions, such as :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileName`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 54-55

In the above example, a modal :sip:ref:`~PyQt6.QtWidgets.QFileDialog` is created using a static function. The dialog initially displays the contents of the "/home/jana" directory, and displays files matching the patterns given in the string "Image Files (\*.png \*.jpg \*.bmp)". The parent of the file dialog is set to *this*, and the window title is set to "Open Image".

If you want to use multiple filters, separate each one with *two* semicolons. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 60-60

You can create your own :sip:ref:`~PyQt6.QtWidgets.QFileDialog` without using the static functions. By calling :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setFileMode`, you can specify what the user must select in the dialog:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 65-66

In the above example, the mode of the file dialog is set to :sip:ref:`~PyQt6.QtWidgets.QFileDialog.FileMode.AnyFile`, meaning that the user can select any file, or even specify a file that doesn't exist. This mode is useful for creating a "Save As" file dialog. Use :sip:ref:`~PyQt6.QtWidgets.QFileDialog.FileMode.ExistingFile` if the user must select an existing file, or :sip:ref:`~PyQt6.QtWidgets.QFileDialog.FileMode.Directory` if only a directory can be selected. See the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.FileMode` enum for the complete list of modes.

The :sip:ref:`~PyQt6.QtWidgets.QFileDialog.fileMode` property contains the mode of operation for the dialog; this indicates what types of objects the user is expected to select. Use :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setNameFilter` to set the dialog's file filter. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 71-71

In the above example, the filter is set to ``"Images (\*.png \*.xpm \*.jpg)"``. This means that only files with the extension ``png``, ``xpm``, or ``jpg`` are shown in the :sip:ref:`~PyQt6.QtWidgets.QFileDialog`. You can apply several filters by using :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setNameFilters`. Use :sip:ref:`~PyQt6.QtWidgets.QFileDialog.selectNameFilter` to select one of the filters you've given as the file dialog's default filter.

The file dialog has two view modes: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.ViewMode.List` and :sip:ref:`~PyQt6.QtWidgets.QFileDialog.ViewMode.Detail`. :sip:ref:`~PyQt6.QtWidgets.QFileDialog.ViewMode.List` presents the contents of the current directory as a list of file and directory names. :sip:ref:`~PyQt6.QtWidgets.QFileDialog.ViewMode.Detail` also displays a list of file and directory names, but provides additional information alongside each name, such as the file size and modification date. Set the mode with :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setViewMode`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 76-76

The last important function you need to use when creating your own file dialog is :sip:ref:`~PyQt6.QtWidgets.QFileDialog.selectedFiles`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 81-83

In the above example, a modal file dialog is created and shown. If the user clicked OK, the file they selected is put in ``fileName``.

The dialog's working directory can be set with :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setDirectory`. Each file in the current directory can be selected using the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.selectFile` function.

The `Standard Dialogs <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_ example shows how to use :sip:ref:`~PyQt6.QtWidgets.QFileDialog` as well as other built-in Qt dialogs.

By default, a platform-native file dialog is used if the platform has one. In that case, the widgets that would otherwise be used to construct the dialog are not instantiated, so related accessors such as layout() and :sip:ref:`~PyQt6.QtWidgets.QFileDialog.itemDelegate` return null. Also, not all platforms show file dialogs with a title bar, so be aware that the caption text might not be visible to the user. You can set the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.DontUseNativeDialog` option or set the :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DontUseNativeDialogs` application attribute to ensure that the widget-based implementation is used instead of the native dialog.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo`, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtWidgets.QColorDialog`, :sip:ref:`~PyQt6.QtWidgets.QFontDialog`, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
