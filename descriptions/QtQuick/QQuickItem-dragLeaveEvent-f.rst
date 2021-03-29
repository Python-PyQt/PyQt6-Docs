.. sip:method-description::
    :status: todo
    :pysig: 6a33903f2425f3a46362f87b7b4da760
    :realsig: (QDragLeaveEvent*)
    :digest: 218daf34c0054b9babc0b598de618e10

This event handler can be reimplemented in a subclass to receive drag-leave events for an item. The event information is provided by the *event* parameter.

Drag and drop events are only provided if the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flags.ItemAcceptsDrops` flag has been set for this item.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.

.. seealso:: `Drag <https://doc.qt.io/qt-6/qml-qtquick-drag.html>`_, `Drag and Drop <https://doc.qt.io/qt-6/dnd.html>`_.
