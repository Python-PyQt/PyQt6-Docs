.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 499ff9f64e7ba48e875cbd9ff4754641

Sets whether the touch points grabbed by this item should remain exclusively with this item.

This is useful for items that wish to grab and keep specific touch points following a predefined gesture. For example, an item that is interested in horizontal touch point movement may set setKeepTouchGrab to true once a threshold has been exceeded. Once setKeepTouchGrab has been set to true, filtering items will not react to the relevant touch points.

If *keep* is false, a filtering item may steal the grab. For example, `Flickable <https://doc.qt.io/qt-6/qml-qtquick-flickable.html>`_ may attempt to steal a touch point grab if it detects that the user has begun to move the viewport.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.keepTouchGrab`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.setKeepMouseGrab`.
