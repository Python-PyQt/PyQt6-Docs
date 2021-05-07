.. sip:method-description::
    :status: todo
    :pysig: cb5c5847dde6df53e0d5179917200bad
    :realsig: (QWidget*,const QString&,const QString&,QMessageBox::StandardButtons,QMessageBox::StandardButton)
    :digest: 567648d5231b48ec4c4adfa96f93cf02

Opens an information message box with the given *title* and *text* in front of the specified *parent* widget.

The standard *buttons* are added to the message box. *defaultButton* specifies the button used when Enter is pressed. *defaultButton* must refer to a button that was given in *buttons*. If *defaultButton* is :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox` chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the :ref:`qmessagebox-default-and-escape-keys` is returned.

The message box is an :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal` dialog box.

**Warning:** Do not delete *parent* during the execution of the dialog. If you want to do this, you should create the dialog yourself using one of the :sip:ref:`~PyQt6.QtWidgets.QMessageBox` constructors.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.question`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.warning`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.critical`.
