.. sip:method-description::
    :status: todo
    :pysig: b02106babcc7b18b77518775f31a161a
    :realsig: (QMessageBox::Option, bool)
    :digest: 3826c642e53f60bc737064a97d7e12af

Sets the given *option* to be enabled if *on* is true; otherwise, clears the given *option*.

Options (particularly the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Option.DontUseNativeDialog` option) should be set before showing the dialog.

Setting options while the dialog is visible is not guaranteed to have an immediate effect on the dialog.

Setting options after changing other properties may cause these values to have no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.options`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.testOption`.
