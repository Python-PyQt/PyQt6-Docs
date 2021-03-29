.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: 9ed93e4f56efc8776cd33b4092895546

Shows the dialog as a modal dialog, blocking until the user closes it. The function returns a :sip:ref:`~PyQt6.QtWidgets.QDialog.DialogCode.DialogCode` result.

If the dialog is :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal`, users cannot interact with any other window in the same application until they close the dialog. If the dialog is :sip:ref:`~PyQt6.QtCore.Qt.WindowModality.ApplicationModal`, only interaction with the parent window is blocked while the dialog is open. By default, the dialog is application modal.

**Note:** Avoid using this function; instead, use ``open()``. Unlike , :sip:ref:`~PyQt6.QtWidgets.QDialog.open` is asynchronous, and does not spin an additional event loop. This prevents a series of dangerous bugs from happening (e.g. deleting the dialog's parent while the dialog is open via ). When using :sip:ref:`~PyQt6.QtWidgets.QDialog.open` you can connect to the :sip:ref:`~PyQt6.QtWidgets.QDialog.finished` signal of :sip:ref:`~PyQt6.QtWidgets.QDialog` to be notified when the dialog is closed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialog.open`, show(), :sip:ref:`~PyQt6.QtWidgets.QDialog.result`, setWindowModality().
