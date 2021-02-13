.. sip:method-description::
    :status: todo
    :pysig: 23d35dcc9a7427560ec99aa97eba883f
    :realsig: (QMessageBox::Icon,const QString&,const QString&,QMessageBox::StandardButtons,QWidget*,Qt::WindowFlags)
    :digest: 8d22534639a9127736fa3d3e66271cb7

Constructs a message box with the given *icon*, *title*, *text*, and standard *buttons*. Standard or custom buttons can be added at any time using :sip:ref:`~PyQt6.QtWidgets.QMessageBox.addButton`. The *parent* and *f* arguments are passed to the :sip:ref:`~PyQt6.QtWidgets.QDialog` constructor.

The message box is an :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal` dialog box.

On macOS, if *parent* is not ``nullptr`` and you want your message box to appear as a :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Sheet` of that parent, set the message box's :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality` to :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.WindowModal` (default). Otherwise, the message box will be a standard dialog.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowTitle`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setText`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setIcon`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setStandardButtons`.
