.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 388668fd096a13f2ea6f047a4d1a2edd

This signal is emitted when the dialog's *result* code has been set, either by the user or by calling :sip:ref:`~PyQt6.QtWidgets.QDialog.done`, :sip:ref:`~PyQt6.QtWidgets.QDialog.accept`, or :sip:ref:`~PyQt6.QtWidgets.QDialog.reject`.

Note that this signal is *not* emitted when hiding the dialog with hide() or :sip:ref:`~PyQt6.QtWidgets.QDialog.setVisible`\ (false). This includes deleting the dialog while it is visible.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialog.accepted`, :sip:ref:`~PyQt6.QtWidgets.QDialog.rejected`.
