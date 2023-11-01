.. sip:method-description::
    :status: todo
    :pysig: fa3a7ff68d581bea35e424a45f00b8ca
    :realsig: (QWidget*, const QString&, const QString&, QMessageBox::StandardButtons, QMessageBox::StandardButton)
    :digest: 83ddd9e6979bc8c2a77f2560236dc5e6

Opens a warning message box with the given *title* and *text* in front of the specified *parent* widget.

The standard *buttons* are added to the message box. *defaultButton* specifies the button used when Enter is pressed. *defaultButton* must refer to a button that was given in *buttons*. If *defaultButton* is :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox` chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the :ref:`qmessagebox-default-and-escape-keys` is returned.

The message box is an :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal` dialog box.

**Warning:** Do not delete *parent* during the execution of the dialog. If you want to do this, you should create the dialog yourself using one of the :sip:ref:`~PyQt6.QtWidgets.QMessageBox` constructors.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.question`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.information`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.critical`.
