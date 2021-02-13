.. sip:method-description::
    :status: todo
    :pysig: a73944383ffd572ba8b60debc3383262
    :realsig: (QWidget*)
    :digest: 2000cb7dd7688cb3f2838d350ae92c70

Constructs a message box with no text and no buttons. *parent* is passed to the :sip:ref:`~PyQt6.QtWidgets.QDialog` constructor.

On macOS, if you want your message box to appear as a :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Sheet` of its *parent*, set the message box's :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowModality` to :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.WindowModal` or use :sip:ref:`~PyQt6.QtWidgets.QMessageBox.open`. Otherwise, the message box will be a standard dialog.
