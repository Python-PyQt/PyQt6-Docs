.. sip:method-description::
    :status: todo
    :pysig: 6002b043d816bb26e32084e9ee07d381
    :realsig: (QWidget*, const QString&, const QString&, QFileDialog::Options)
    :digest: 28ab3575d2685c3116cf99b225ab13d4

This is a convenience static function that returns an existing directory selected by the user.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 128-131

This function creates a modal file dialog with the given *parent* widget. If *parent* is not ``nullptr``, the dialog is shown centered over the parent widget.

The dialog's working directory is set to *dir*, and the caption is set to *caption*. Either of these can be an empty string in which case the current directory and a default caption are used respectively.

The *options* argument holds various options about how to run the dialog. See the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option` enum for more information on the flags you can pass. To ensure a native file dialog, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.ShowDirsOnly` must be set.

On Windows and macOS, this static function uses the native file dialog and not a :sip:ref:`~PyQt6.QtWidgets.QFileDialog`. However, the native Windows file dialog does not support displaying files in the directory chooser. You need to pass the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.DontUseNativeDialog` option, or set the global \\l{Qt::}{AA_DontUseNativeDialogs} application attribute to display files using a :sip:ref:`~PyQt6.QtWidgets.QFileDialog`.

Note that the macOS native file dialog does not show a title bar.

On Unix/X11, the normal behavior of the file dialog is to resolve and follow symlinks. For example, if ``/usr/tmp`` is a symlink to ``/var/tmp``, the file dialog changes to ``/var/tmp`` after entering ``/usr/tmp``. If *options* includes :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.DontResolveSymlinks`, the file dialog treats symlinks as regular directories.

On Windows, the dialog spins a blocking modal event loop that does not dispatch any QTimers, and if *parent* is not ``nullptr`` then it positions the dialog just below the parent's title bar.

**Warning:** Do not delete *parent* during the execution of the dialog. If you want to do this, you must create the dialog yourself using one of the :sip:ref:`~PyQt6.QtWidgets.QFileDialog` constructors.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileName`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileNames`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getSaveFileName`.
