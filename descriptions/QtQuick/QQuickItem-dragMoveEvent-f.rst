.. sip:method-description::
    :status: todo
    :pysig: d7df8911371a132d515a4c7922037f8f
    :realsig: (QDragMoveEvent*)
    :digest: b906315ed187d89843832a82a7cc98fb

This event handler can be reimplemented in a subclass to receive drag-move events for an item. The event information is provided by the *event* parameter.

Drag and drop events are only provided if the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flags.ItemAcceptsDrops` flag has been set for this item.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

.. seealso:: `Drag <https://doc.qt.io/qt-6/qml-qtquick-drag.html>`_, `Drag and Drop <https://doc.qt.io/qt-6/dnd.html>`_.
