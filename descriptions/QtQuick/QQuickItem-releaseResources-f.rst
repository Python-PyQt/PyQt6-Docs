.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ea0b3bde80b89a88eaae061fab38a7b9

This function is called when an item should release graphics resources which are not already managed by the nodes returned from :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode`.

This happens when the item is about to be removed from the window it was previously rendering to. The item is guaranteed to have a :sip:ref:`~PyQt6.QtQuick.QQuickItem.window` when the function is called.

The function is called on the GUI thread and the state of the rendering thread, when it is used, is unknown. Objects should not be deleted directly, but instead scheduled for cleanup using :sip:ref:`~PyQt6.QtQuick.QQuickWindow.scheduleRenderJob`.

.. seealso:: :ref:`qquickitem-graphics-resource-handling`.
