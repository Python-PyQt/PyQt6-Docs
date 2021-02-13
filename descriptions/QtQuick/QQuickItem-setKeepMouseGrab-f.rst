.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 5174d32909662dbc34344c024bfa02d3

Sets whether the mouse input should remain exclusively with this item.

This is useful for items that wish to grab and keep mouse interaction following a predefined gesture. For example, an item that is interested in horizontal mouse movement may set :sip:ref:`~PyQt6.QtQuick.QQuickItem.keepMouseGrab` to true once a threshold has been exceeded. Once :sip:ref:`~PyQt6.QtQuick.QQuickItem.keepMouseGrab` has been set to true, filtering items will not react to mouse events.

If *keep* is false, a filtering item may steal the grab. For example, `Flickable <https://doc.qt.io/qt-6/qml-qtquick-flickable.html>`_ may attempt to steal a mouse grab if it detects that the user has begun to move the viewport.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.keepMouseGrab`.
