.. sip:method-description::
    :status: todo
    :pysig: 109337c6a1170745db57e104880cc590
    :realsig: (QFileDialog::Option,bool)
    :digest: ce16eb83f922642ec8b2f4785831d1d1

Sets the given *option* to be enabled if *on* is true; otherwise, clears the given *option*.

Options (particularly the :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Option.DontUseNativeDialog` option) should be set before changing dialog properties or showing the dialog.

Setting options while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).

Setting options after changing other properties may cause these values to have no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.options`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.testOption`.
