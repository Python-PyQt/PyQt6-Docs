.. sip:method-description::
    :status: todo
    :pysig: 23d35dcc9a7427560ec99aa97eba883f
    :realsig: (QMessageBox::Icon,const QString&,const QString&,QMessageBox::StandardButtons,QWidget*,Qt::WindowFlags)
    :digest: f44e701c9a5571863d798d324b088a47

Constructs an :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal` message box with the given *icon*, *title*, *text*, and standard *buttons*. Standard or custom buttons can be added at any time using :sip:ref:`~PyQt6.QtWidgets.QMessageBox.addButton`. The *parent* and *f* arguments are passed to the :sip:ref:`~PyQt6.QtWidgets.QDialog` constructor.

The window modality can be overridden via :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality` before calling show().

**Note:** Using :sip:ref:`~PyQt6.QtWidgets.QMessageBox.open` or exec() to show the message box affects the window modality. Please see the detailed documentation for each function for more information.

On macOS, if *parent* is not ``nullptr`` and you want your message box to appear as a :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Sheet` of that parent, set the message box's :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality` to :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.WindowModal` (default). Otherwise, the message box will be a standard dialog.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowTitle`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setText`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setIcon`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setStandardButtons`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality`.
