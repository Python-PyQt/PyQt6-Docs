.. sip:class-description::
    :status: todo
    :brief: Contains event parameters for child object events
    :digest: 066fa54c40fee7e8679bb20ddca51057

The :sip:ref:`~PyQt6.QtCore.QChildEvent` class contains event parameters for child object events.

Child events are sent immediately to objects when children are added or removed.

In both cases you can only rely on the child being a :sip:ref:`~PyQt6.QtCore.QObject` (or, if :sip:ref:`~PyQt6.QtCore.QObject.isWidgetType` returns ``true``, a QWidget). This is because in the :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildAdded` case the child is not yet fully constructed; in the :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildRemoved` case it might have already been destructed.

The handler for these events is :sip:ref:`~PyQt6.QtCore.QObject.childEvent`.
