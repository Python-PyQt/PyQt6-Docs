.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: b81e5c4083eda029789a0d4bc7108bf9

Closes the dialog and sets its result code to *r*. The :sip:ref:`~PyQt6.QtWidgets.QDialog.finished` signal will emit *r*; if *r* is :sip:ref:`~PyQt6.QtWidgets.QDialog.DialogCode.Accepted` or :sip:ref:`~PyQt6.QtWidgets.QDialog.DialogCode.Rejected`, the :sip:ref:`~PyQt6.QtWidgets.QDialog.accepted` or the :sip:ref:`~PyQt6.QtWidgets.QDialog.rejected` signals will also be emitted, respectively.

If this dialog is shown with :sip:ref:`~PyQt6.QtWidgets.QDialog.exec`,  also causes the local event loop to finish, and :sip:ref:`~PyQt6.QtWidgets.QDialog.exec` to return *r*.

As with :sip:ref:`~PyQt6.QtWidgets.QWidget.close`,  deletes the dialog if the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose` flag is set. If the dialog is the application's main widget, the application terminates. If the dialog is the last window closed, the QApplication::lastWindowClosed() signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialog.accept`, :sip:ref:`~PyQt6.QtWidgets.QDialog.reject`, :sip:ref:`~PyQt6.QtWidgets.QApplication.activeWindow`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`.
