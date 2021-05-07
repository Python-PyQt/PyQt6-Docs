.. sip:method-description::
    :status: todo
    :pysig: 54325e9368999a85b6b186618ee81876
    :realsig: (Qt::MouseButtons)
    :digest: a4425d1c7291f2376ff3435bd751a6f0

Sets the mouse buttons accepted by this item to *buttons*.

**Note:** In Qt 5, calling  implicitly caused an item to receive touch events as well as mouse events; but it was recommended to call :sip:ref:`~PyQt6.QtQuick.QQuickItem.setAcceptTouchEvents` to subscribe for them. In Qt 6, it is necessary to call :sip:ref:`~PyQt6.QtQuick.QQuickItem.setAcceptTouchEvents` to continue to receive them.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.acceptedMouseButtons`.
