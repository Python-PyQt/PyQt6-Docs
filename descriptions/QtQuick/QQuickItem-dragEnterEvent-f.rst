.. sip:method-description::
    :status: todo
    :pysig: 8708b1d9b8a1d0e5467b1ef89589d7cc
    :realsig: (QDragEnterEvent*)
    :digest: 2e8c88ab06f7ab09669514fea9c489da

This event handler can be reimplemented in a subclass to receive drag-enter events for an item. The event information is provided by the *event* parameter.

Drag and drop events are only provided if the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flags.ItemAcceptsDrops` flag has been set for this item.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

.. seealso:: `Drag <https://doc.qt.io/qt-6/qml-qtquick-drag.html>`_, `Drag and Drop <https://doc.qt.io/qt-6/dnd.html>`_.
