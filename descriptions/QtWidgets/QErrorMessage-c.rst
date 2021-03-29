.. sip:class-description::
    :status: todo
    :brief: Error message display dialog
    :digest: 160aaf213db2110072194b8b64601f8e

The :sip:ref:`~PyQt6.QtWidgets.QErrorMessage` class provides an error message display dialog.

An error message widget consists of a text label and a checkbox. The checkbox lets the user control whether the same error message will be displayed again in the future, typically displaying the text, "Show this message again" translated into the appropriate local language.

For production applications, the class can be used to display messages which the user only needs to see once. To use :sip:ref:`~PyQt6.QtWidgets.QErrorMessage` like this, you create the dialog in the usual way, and show it by calling the :sip:ref:`~PyQt6.QtWidgets.QErrorMessage.showMessage` slot or connecting signals to it.

The static :sip:ref:`~PyQt6.QtWidgets.QErrorMessage.qtHandler` function installs a message handler using :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler` and creates a :sip:ref:`~PyQt6.QtWidgets.QErrorMessage` that displays :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qWarning` and :sip:ref:`~PyQt6.QtCore.qFatal` messages. This is most useful in environments where no console is available to display warnings and error messages.

In both cases :sip:ref:`~PyQt6.QtWidgets.QErrorMessage` will queue pending messages and display them in order, with each new message being shown as soon as the user has accepted the previous message. Once the user has specified that a message is not to be shown again it is automatically skipped, and the dialog will show the next appropriate message in the queue.

The `Standard Dialogs <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_ example shows how to use :sip:ref:`~PyQt6.QtWidgets.QErrorMessage` as well as other built-in Qt dialogs.

.. image:: ../../../images/qerrormessage.png

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.showMessage`, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
