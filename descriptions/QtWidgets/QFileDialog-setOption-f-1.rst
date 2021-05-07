.. sip:method-description::
    :status: todo
    :pysig: a115fa94df387c8fd18c53af081444e7
    :realsig: (QFileDialog::Option,bool)
    :digest: 8ca88d896f624d16b2f4404c9d517bc5

Sets the given *option* to be enabled if *on* is true; otherwise, clears the given *option*.

Options (particularly the DontUseNativeDialogs option) should be set before changing dialog properties or showing the dialog.

Setting options while the dialog is visible is not guaranteed to have an immediate effect on the dialog (depending on the option and on the platform).

Setting options after changing other properties may cause these values to have no effect.

.. seealso:: `options <https://doc.qt.io/qt-6/qt-wrap-ui.html#options>`_, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.testOption`.
