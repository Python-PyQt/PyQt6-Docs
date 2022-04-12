.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d8628d84011c2ef02713f0a7a14d395a

This function should perform any layout as required for this item.

When :sip:ref:`~PyQt6.QtQuick.QQuickItem.polish` is called, the scene graph schedules a polish event for this item. When the scene graph is ready to render this item, it calls  to do any item layout as required before it renders the next frame.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.ensurePolished`.
