.. sip:class-description::
    :status: todo
    :brief: Contains event parameters for child object events
    :digest: 6967b375e6449e198df9f252df20453f

The :sip:ref:`~PyQt6.QtCore.QChildEvent` class contains event parameters for child object events.

Child events are sent immediately to objects when children are added or removed.

In both cases you can only rely on the child being a :sip:ref:`~PyQt6.QtCore.QObject` (or, if :sip:ref:`~PyQt6.QtCore.QObject.isWidgetType` returns ``true``, a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_). This is because in the :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildAdded` case the child is not yet fully constructed; in the :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildRemoved` case it might have already been destructed.

The handler for these events is :sip:ref:`~PyQt6.QtCore.QObject.childEvent`.
