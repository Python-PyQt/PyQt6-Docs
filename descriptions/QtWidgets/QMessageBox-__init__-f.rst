.. sip:method-description::
    :status: todo
    :pysig: a73944383ffd572ba8b60debc3383262
    :realsig: (QWidget*)
    :digest: 16805e26e31a70df0e3a985cc275fa54

Constructs an :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal` message box with no text and no buttons. *parent* is passed to the :sip:ref:`~PyQt6.QtWidgets.QDialog` constructor.

The window modality can be overridden via :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality` before calling show().

**Note:** Using :sip:ref:`~PyQt6.QtWidgets.QMessageBox.open` or exec() to show the message box affects the window modality. Please see the detailed documentation for each function for more information.

On macOS, if you want your message box to appear as a :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Sheet` of its *parent*, set the message box's :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality` to :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.WindowModal` or use :sip:ref:`~PyQt6.QtWidgets.QMessageBox.open`. Otherwise, the message box will be a standard dialog.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowTitle`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setText`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setIcon`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setStandardButtons`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality`.
