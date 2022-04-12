.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f0938c144aed9d6702b71e291020a7b2

Calls :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePolish`

This can be useful for items such as Layouts (or Positioners) which delay calculation of their :sip:ref:`~PyQt6.QtQuick.QQuickItem.implicitWidth` and :sip:ref:`~PyQt6.QtQuick.QQuickItem.implicitHeight` until they receive a PolishEvent.

Normally, if e.g. a child item is added or removed to a Layout, the implicit size is not immediately calculated (this is an optimization). In some cases it might be desirable to query the implicit size of the layout right after a child item has been added. If this is the case, use this function right before querying the implicit size.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePolish`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.polish`.
