.. sip:method-description::
    :status: todo
    :pysig: 7a24eddeb2949cd08097183512577f70
    :realsig: (QMessageBox::StandardButton) const
    :digest: c24623fee32cc5105b03d462df5be283

Returns a pointer corresponding to the standard button *which*, or ``nullptr`` if the standard button doesn't exist in this message box.

**Note:** Modifying the properties of the returned button may not be reflected in native implementations of the message dialog. To customize dialog buttons add a custom button or button title instead, or set the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Option.DontUseNativeDialog` option.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.standardButtons`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.standardButton`.
