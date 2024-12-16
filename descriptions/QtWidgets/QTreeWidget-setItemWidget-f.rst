.. sip:method-description::
    :status: todo
    :pysig: da2e56a00b946a83463a878480c21bea
    :realsig: (QTreeWidgetItem*,int,QWidget*)
    :digest: b42273bd3e1beb4d035f1eecb9e82748

Sets the given *widget* to be displayed in the cell specified by the given *item* and *column*.

The given *widget*'s :sip:ref:`~PyQt6.QtWidgets.QWidget.autoFillBackground` property must be set to true, otherwise the widget's background will be transparent, showing both the model data and the tree widget item.

This function should only be used to display static content in the place of a tree widget item. If you want to display custom dynamic content or implement a custom editor widget, use :sip:ref:`~PyQt6.QtWidgets.QTreeView` and subclass :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` instead.

This function cannot be called before the item hierarchy has been set up, i.e., the :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem` that will hold *widget* must have been added to the view before *widget* is set.

**Note:** The tree takes ownership of *widget*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.itemWidget`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.removeItemWidget`, `Delegate Classes <https://doc.qt.io/qt-6/model-view-programming.html#delegate-classes>`_.
