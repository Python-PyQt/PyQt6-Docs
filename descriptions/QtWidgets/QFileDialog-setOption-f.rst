.. sip:method-description::
    :status: todo
    :pysig: 109337c6a1170745db57e104880cc590
    :realsig: (QFileDialog::Option,bool)
    :digest: 8ca88d896f624d16b2f4404c9d517bc5

Sets the given *option* to be enabled if *on* is true; otherwise, clears the given *option*.

Options (particularly the DontUseNativeDialogs option) should be set before changing dialog properties or showing the dialog.

Setting options while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).

Setting options after changing other properties may cause these values to have no effect.

.. seealso:: `options <https://doc.qt.io/qt-6/qt-wrap-ui.html#options>`_, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.testOption`.
