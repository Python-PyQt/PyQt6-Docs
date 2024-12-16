.. sip:method-description::
    :status: todo
    :pysig: 1fdaa3f82e7a324487f622d983d9aa9d
    :realsig: (QListWidgetItem*,QWidget*)
    :digest: 60544b4d509388980fc03bf60cf7eb00

Sets the *widget* to be displayed in the given *item*.

This function should only be used to display static content in the place of a list widget item. If you want to display custom dynamic content or implement a custom editor widget, use :sip:ref:`~PyQt6.QtWidgets.QListView` and subclass :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` instead.

**Note:** The list takes ownership of the *widget*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListWidget.itemWidget`, :sip:ref:`~PyQt6.QtWidgets.QListWidget.removeItemWidget`, `Delegate Classes <https://doc.qt.io/qt-6/model-view-programming.html#delegate-classes>`_.
