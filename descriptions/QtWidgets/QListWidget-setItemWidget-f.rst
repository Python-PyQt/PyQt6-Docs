.. sip:method-description::
    :status: todo
    :pysig: 1fdaa3f82e7a324487f622d983d9aa9d
    :realsig: (QListWidgetItem*,QWidget*)
    :digest: e109fef2ef5c1f84f2969c99d598c85d

Sets the *widget* to be displayed in the given *item*.

This function should only be used to display static content in the place of a list widget item. If you want to display custom dynamic content or implement a custom editor widget, use :sip:ref:`~PyQt6.QtWidgets.QListView` and subclass :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListWidget.itemWidget`, :sip:ref:`~PyQt6.QtWidgets.QListWidget.removeItemWidget`, `Delegate Classes <https://doc.qt.io/qt-6/model-view-programming.html#delegate-classes>`_.
