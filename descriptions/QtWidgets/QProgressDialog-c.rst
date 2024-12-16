.. sip:class-description::
    :status: todo
    :brief: Feedback on the progress of a slow operation
    :digest: 040f2c5195c6c7edaeb05d332306c19e

The :sip:ref:`~PyQt6.QtWidgets.QProgressDialog` class provides feedback on the progress of a slow operation.

A progress dialog is used to give the user an indication of how long an operation is going to take, and to demonstrate that the application has not frozen. It can also give the user an opportunity to abort the operation.

A common problem with progress dialogs is that it is difficult to know when to use them; operations take different amounts of time on different hardware. :sip:ref:`~PyQt6.QtWidgets.QProgressDialog` offers a solution to this problem: it estimates the time the operation will take (based on time for steps), and only shows itself if that estimate is beyond :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.minimumDuration` (4 seconds by default).

Use :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMinimum` and :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMaximum` or the constructor to set the number of "steps" in the operation and call :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue` as the operation progresses. The number of steps can be chosen arbitrarily. It can be the number of files copied, the number of bytes received, the number of iterations through the main loop of your algorithm, or some other suitable unit. Progress starts at the value set by :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMinimum`, and the progress dialog shows that the operation has finished when you call :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue` with the value set by :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMaximum` as its argument.

The dialog automatically resets and hides itself at the end of the operation. Use :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setAutoReset` and :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setAutoClose` to change this behavior. Note that if you set a new maximum (using :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMaximum` or :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setRange`) that equals your current :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.value`, the dialog will not close regardless.

There are two ways of using :sip:ref:`~PyQt6.QtWidgets.QProgressDialog`: modal and modeless.

Compared to a modeless :sip:ref:`~PyQt6.QtWidgets.QProgressDialog`, a modal :sip:ref:`~PyQt6.QtWidgets.QProgressDialog` is simpler to use for the programmer. Do the operation in a loop, call :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue` at intervals, and check for cancellation with :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.wasCanceled`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-dialogs-dialogs.py
    :lines: 222-232

A modeless progress dialog is suitable for operations that take place in the background, where the user is able to interact with the application. Such operations are typically based on a timer class, such as QChronoTimer (or the more low-level :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`) or :sip:ref:`~PyQt6.QtCore.QSocketNotifier`; or performed in a separate thread. A :sip:ref:`~PyQt6.QtWidgets.QProgressBar` in the status bar of your main window is often an alternative to a modeless progress dialog.

You need to have an event loop to be running, connect the :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.canceled` signal to a slot that stops the operation, and call :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue` at intervals. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-dialogs-dialogs.py
    :lines: 250-259

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-dialogs-dialogs.py
    :lines: 261-269

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-dialogs-dialogs.py
    :lines: 271-276

In both modes the progress dialog may be customized by replacing the child widgets with custom widgets by using :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setLabel`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setBar`, and :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setCancelButton`. The functions :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setLabelText` and :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setCancelButtonText` set the texts shown.

.. image:: ../../../images/fusion-progressdialog.png

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialog`, :sip:ref:`~PyQt6.QtWidgets.QProgressBar`.
