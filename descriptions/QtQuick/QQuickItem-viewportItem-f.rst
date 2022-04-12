.. sip:method-description::
    :status: todo
    :pysig: a0867d3002630bbad6e7e3985f19f7f9
    :realsig: () const
    :digest: 587a356250ff74c564c0c960a2fb6792

If the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flag.ItemObservesViewport` flag is set, returns the nearest parent with the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flag.ItemIsViewport` flag. Returns the window's contentItem if the flag is not set, or if no other viewport item is found.

Returns ``nullptr`` only if there is no viewport item and this item is not shown in a window.

.. seealso:: clipRect().
