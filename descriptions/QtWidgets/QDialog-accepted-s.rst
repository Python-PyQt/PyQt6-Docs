.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: adca44d9221f1377da5393684edf7b38

This signal is emitted when the dialog has been accepted either by the user or by calling :sip:ref:`~PyQt6.QtWidgets.QDialog.accept` or :sip:ref:`~PyQt6.QtWidgets.QDialog.done` with the :sip:ref:`~PyQt6.QtWidgets.QDialog.DialogCode.Accepted` argument.

Note that this signal is *not* emitted when hiding the dialog with hide() or :sip:ref:`~PyQt6.QtWidgets.QDialog.setVisible`\ (false). This includes deleting the dialog while it is visible.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialog.finished`, :sip:ref:`~PyQt6.QtWidgets.QDialog.rejected`.
