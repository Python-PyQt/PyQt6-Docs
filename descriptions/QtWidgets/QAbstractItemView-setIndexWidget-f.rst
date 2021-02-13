.. sip:method-description::
    :status: todo
    :pysig: 9f2b33ec75e327b2ae1c357d3c6f9fb5
    :realsig: (const QModelIndex&,QWidget*)
    :digest: cb73c4304628f0e2265d2b9bd59ff451

Sets the given *widget* on the item at the given *index*, passing the ownership of the widget to the viewport.

If *index* is invalid (e.g., if you pass the root index), this function will do nothing.

The given *widget*'s `autoFillBackground <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ property must be set to true, otherwise the widget's background will be transparent, showing both the model data and the item at the given *index*.

If index widget A is replaced with index widget B, index widget A will be deleted. For example, in the code snippet below, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit` object will be deleted.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qabstractitemview.py
    :lines: 61-63

This function should only be used to display static content within the visible area corresponding to an item of data. If you want to display custom dynamic content or implement a custom editor widget, subclass :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.indexWidget`, `Delegate Classes <https://doc.qt.io/qt-6/model-view-programming.html#delegate-classes>`_.
