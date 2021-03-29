.. sip:method-description::
    :status: todo
    :pysig: 57ac5479d26d935dcda6b53048f4e0f8
    :realsig: (const QColor&)
    :digest: 7252dec0132e76188cf743b4c425cfd5

Sets the clear *color*. By default this is an opaque color.

To get a semi-transparent :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`, call this function with *color* set to :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.transparent`, set the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_TranslucentBackground` widget attribute on the top-level window, and request an alpha channel via :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.setFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setColor`.
