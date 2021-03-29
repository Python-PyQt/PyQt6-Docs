.. sip:method-description::
    :status: todo
    :pysig: f46cc8bb8d9029504f83ecdd62d53e40
    :realsig: () const
    :digest: 91548592443a312abe605ceae33ccb6b

Returns the button that is activated when escape is pressed.

By default, :sip:ref:`~PyQt6.QtWidgets.QMessageBox` attempts to automatically detect an escape button as follows:

#. If there is only one button, it is made the escape button.

#. If there is a :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.Cancel` button, it is made the escape button.

#. On macOS only, if there is exactly one button with the role :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole.RejectRole`, it is made the escape button.

When an escape button could not be automatically detected, pressing Esc has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setEscapeButton`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.addButton`.
