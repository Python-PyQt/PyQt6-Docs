.. sip:method-description::
    :status: todo
    :pysig: 6002b043d816bb26e32084e9ee07d381
    :realsig: (QWidget*, const QString&, const QString&, QFileDialog::Options)
    :digest: 185e376fcbf6c5209a0431cebf70e584

This is a convenience static function that will return an existing directory selected by the user.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 128-131

This function creates a modal file dialog with the given *parent* widget. If *parent* is not ``nullptr``, the dialog will be shown centered over the parent widget.

The dialog's working directory is set to *dir*, and the caption is set to *caption*. Either of these may be an empty string in which case the current directory and a default caption will be used respectively.

The *options* argument holds various options about how to run the dialog, see the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option` enum for more information on the flags you can pass. To ensure a native file dialog, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.ShowDirsOnly` must be set.

On Windows and macOS, this static function will use the native file dialog and not a :sip:ref:`~PyQt6.QtWidgets.QFileDialog`. However, the native Windows file dialog does not support displaying files in the directory chooser. You need to pass :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.DontUseNativeDialog` to display files using a :sip:ref:`~PyQt6.QtWidgets.QFileDialog`.

Note that the macOS native file dialog does not show a title bar.

On Unix/X11, the normal behavior of the file dialog is to resolve and follow symlinks. For example, if ``/usr/tmp`` is a symlink to ``/var/tmp``, the file dialog will change to ``/var/tmp`` after entering ``/usr/tmp``. If *options* includes :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.DontResolveSymlinks`, the file dialog will treat symlinks as regular directories.

On Windows, the dialog will spin a blocking modal event loop that will not dispatch any QTimers, and if *parent* is not ``nullptr`` then it will position the dialog just below the parent's title bar.

**Warning:** Do not delete *parent* during the execution of the dialog. If you want to do this, you should create the dialog yourself using one of the :sip:ref:`~PyQt6.QtWidgets.QFileDialog` constructors.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileName`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileNames`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getSaveFileName`.
