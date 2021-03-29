.. sip:method-description::
    :status: todo
    :pysig: 2e04353ee2287b6f1902567288f62896
    :realsig: (QDropEvent*)
    :digest: 7f3b48ec8ada58649130926c8cce4ee4

This event handler can be reimplemented in a subclass to receive drop events for an item. The event information is provided by the *event* parameter.

Drag and drop events are only provided if the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flags.ItemAcceptsDrops` flag has been set for this item.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

.. seealso:: `Drag <https://doc.qt.io/qt-6/qml-qtquick-drag.html>`_, `Drag and Drop <https://doc.qt.io/qt-6/dnd.html>`_.
