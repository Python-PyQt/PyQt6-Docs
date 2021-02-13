.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 7f2530e2ce2f26457dd345a76647bcec

Sets whether the touch points grabbed by this item should remain exclusively with this item.

This is useful for items that wish to grab and keep specific touch points following a predefined gesture. For example, an item that is interested in horizontal touch point movement may set  to true once a threshold has been exceeded. Once  has been set to true, filtering items will not react to the relevant touch points.

If *keep* is false, a filtering item may steal the grab. For example, `Flickable <https://doc.qt.io/qt-6/qml-qtquick-flickable.html>`_ may attempt to steal a touch point grab if it detects that the user has begun to move the viewport.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.keepTouchGrab`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.setKeepMouseGrab`.
