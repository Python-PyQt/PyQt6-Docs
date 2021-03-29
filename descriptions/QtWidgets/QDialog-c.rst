.. sip:class-description::
    :status: todo
    :brief: The base class of dialog windows
    :digest: 817e4225119e3318e1192015ad77625f

The :sip:ref:`~PyQt6.QtWidgets.QDialog` class is the base class of dialog windows.

A dialog window is a top-level window mostly used for short-term tasks and brief communications with the user. QDialogs may be modal or modeless. QDialogs can provide a return value, and they can have default buttons. QDialogs can also have a :sip:ref:`~PyQt6.QtWidgets.QSizeGrip` in their lower-right corner, using :sip:ref:`~PyQt6.QtWidgets.QDialog.setSizeGripEnabled`.

Note that :sip:ref:`~PyQt6.QtWidgets.QDialog` (and any other widget that has type ``Qt::Dialog``) uses the parent widget slightly differently from other classes in Qt. A dialog is always a top-level widget, but if it has a parent, its default location is centered on top of the parent's top-level widget (if it is not top-level itself). It will also share the parent's taskbar entry.

Use the overload of the :sip:ref:`~PyQt6.QtWidgets.QWidget.setParent` function to change the ownership of a :sip:ref:`~PyQt6.QtWidgets.QDialog` widget. This function allows you to explicitly set the window flags of the reparented widget; using the overloaded function will clear the window flags specifying the window-system properties for the widget (in particular it will reset the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Dialog` flag).

**Note:** The parent relationship of the dialog does *not* imply that the dialog will always be stacked on top of the parent window. To ensure that the dialog is always on top, make the dialog modal. This also applies for child windows of the dialog itself. To ensure that child windows of the dialog stay on top of the dialog, make the child windows modal as well.

.. _qdialog-modal-dialogs:

Modal Dialogs
-------------

A **modal** dialog is a dialog that blocks input to other visible windows in the same application. Dialogs that are used to request a file name from the user or that are used to set application preferences are usually modal. Dialogs can be :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal` (the default) or :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.WindowModal`.

When an application modal dialog is opened, the user must finish interacting with the dialog and close it before they can access any other window in the application. Window modal dialogs only block access to the window associated with the dialog, allowing the user to continue to use other windows in an application.

The most common way to display a modal dialog is to call its :sip:ref:`~PyQt6.QtWidgets.QDialog.exec` function. When the user closes the dialog, :sip:ref:`~PyQt6.QtWidgets.QDialog.exec` will provide a useful return value. To close the dialog and return the appropriate value, you must connect a default button, e.g. an OK button to the :sip:ref:`~PyQt6.QtWidgets.QDialog.accept` slot and a Cancel button to the :sip:ref:`~PyQt6.QtWidgets.QDialog.reject` slot. Alternatively, you can call the :sip:ref:`~PyQt6.QtWidgets.QDialog.done` slot with ``Accepted`` or ``Rejected``.

An alternative is to call :sip:ref:`~PyQt6.QtWidgets.QDialog.setModal`\ (true) or setWindowModality(), then show(). Unlike :sip:ref:`~PyQt6.QtWidgets.QDialog.exec`, show() returns control to the caller immediately. Calling :sip:ref:`~PyQt6.QtWidgets.QDialog.setModal`\ (true) is especially useful for progress dialogs, where the user must have the ability to interact with the dialog, e.g. to cancel a long running operation. If you use show() and :sip:ref:`~PyQt6.QtWidgets.QDialog.setModal`\ (true) together to perform a long operation, you must call :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents` periodically during processing to enable the user to interact with the dialog. (See :sip:ref:`~PyQt6.QtWidgets.QProgressDialog`.)

.. _qdialog-modeless-dialogs:

Modeless Dialogs
----------------

A **modeless** dialog is a dialog that operates independently of other windows in the same application. Find and replace dialogs in word-processors are often modeless to allow the user to interact with both the application's main window and with the dialog.

Modeless dialogs are displayed using show(), which returns control to the caller immediately.

If you invoke the :sip:ref:`~PyQt6.QtWidgets.QWidget.show` function after hiding a dialog, the dialog will be displayed in its original position. This is because the window manager decides the position for windows that have not been explicitly placed by the programmer. To preserve the position of a dialog that has been moved by the user, save its position in your :sip:ref:`~PyQt6.QtWidgets.QWidget.closeEvent` handler and then move the dialog to that position, before showing it again.

.. _qdialog-default:

.. _qdialog-default-button:

Default Button
--------------

A dialog's *default* button is the button that's pressed when the user presses Enter (Return). This button is used to signify that the user accepts the dialog's settings and wants to close the dialog. Use :sip:ref:`~PyQt6.QtWidgets.QPushButton.setDefault`, :sip:ref:`~PyQt6.QtWidgets.QPushButton.isDefault` and :sip:ref:`~PyQt6.QtWidgets.QPushButton.autoDefault` to set and control the dialog's default button.

.. _qdialog-escapekey:

.. _qdialog-escape-key:

Escape Key
----------

If the user presses the Esc key in a dialog, :sip:ref:`~PyQt6.QtWidgets.QDialog.reject` will be called. This will cause the window to close: The :sip:ref:`~PyQt6.QtGui.QCloseEvent` cannot be :sip:ref:`~PyQt6.QtCore.QEvent.ignore`.

.. _qdialog-extensibility:

Extensibility
-------------

Extensibility is the ability to show the dialog in two ways: a partial dialog that shows the most commonly used options, and a full dialog that shows all the options. Typically an extensible dialog will initially appear as a partial dialog, but with a More toggle button. If the user presses the More button down, the dialog is expanded. The `Extension Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-extension-example.html>`_ shows how to achieve extensible dialogs using Qt.

.. _qdialog-return:

.. _qdialog-return-value-modal-dialogs:

Return Value (Modal Dialogs)
----------------------------

Modal dialogs are often used in situations where a return value is required, e.g. to indicate whether the user pressed OK or Cancel. A dialog can be closed by calling the :sip:ref:`~PyQt6.QtWidgets.QDialog.accept` or the :sip:ref:`~PyQt6.QtWidgets.QDialog.reject` slots, and :sip:ref:`~PyQt6.QtWidgets.QDialog.exec` will return ``Accepted`` or ``Rejected`` as appropriate. The :sip:ref:`~PyQt6.QtWidgets.QDialog.exec` call returns the result of the dialog. The result is also available from :sip:ref:`~PyQt6.QtWidgets.QDialog.result` if the dialog has not been destroyed.

In order to modify your dialog's close behavior, you can reimplement the functions :sip:ref:`~PyQt6.QtWidgets.QDialog.accept`, :sip:ref:`~PyQt6.QtWidgets.QDialog.reject` or :sip:ref:`~PyQt6.QtWidgets.QDialog.done`. The :sip:ref:`~PyQt6.QtWidgets.QWidget.closeEvent` function should only be reimplemented to preserve the dialog's position or to override the standard close or reject behavior.

.. _qdialog-examples:

.. _qdialog-code-examples:

Code Examples
-------------

A modal dialog:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-dialogs-dialogs.py
    :lines: 92-97

A modeless dialog:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-dialogs-dialogs.py
    :lines: 77-88

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox`, :sip:ref:`~PyQt6.QtWidgets.QTabWidget`, `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog`, `GUI Design Handbook: Dialogs, Standard <https://doc.qt.io/qt-6/guibooks.html#fowler>`_, `Extension Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-extension-example.html>`_, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
