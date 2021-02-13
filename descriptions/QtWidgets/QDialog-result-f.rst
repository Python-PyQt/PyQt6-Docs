.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 3bcd1494c2349408d8ee77e79ab3606b

In general returns the modal dialog's result code, ``Accepted`` or ``Rejected``.

**Note:** When called on a :sip:ref:`~PyQt6.QtWidgets.QMessageBox` instance, the returned value is a value of the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` enum.

Do not call this function if the dialog was constructed with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose` attribute.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialog.setResult`.
