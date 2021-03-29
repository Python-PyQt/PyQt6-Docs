.. sip:method-description::
    :status: todo
    :pysig: 661a8ba71eddf699c3a14cbe92842d88
    :realsig: (const QSizePolicy&)
    :digest: d73604103780165ae6a99ac54f757b14

Sets the size policy to *policy*. The size policy describes how the item should grow horizontally and vertically when arranged in a layout.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem`'s default size policy is (\ :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy.Fixed`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy.Fixed`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.ControlTypes.DefaultType`), but it is common for subclasses to change the default. For example, `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ defaults to (\ :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy.Preferred`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy.Preferred`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.ControlTypes.DefaultType`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizePolicy`, :sip:ref:`~PyQt6.QtWidgets.QWidget.sizePolicy`.
