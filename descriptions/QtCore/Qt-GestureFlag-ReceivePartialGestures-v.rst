.. sip:enum-member-description::
    :status: todo
    :value: 0x02
    :digest: 38f01fa45e619f651bf0acd3d213d6c3

Allows any ignored gesture events to be propagated to parent widgets which have specified this hint. By default only gestures that are in the :sip:ref:`~PyQt6.QtCore.Qt.GestureState.GestureStarted` state are propagated and the widget always gets the full gesture sequence starting with a gesture in the :sip:ref:`~PyQt6.QtCore.Qt.GestureState.GestureStarted` state and ending with a gesture in the :sip:ref:`~PyQt6.QtCore.Qt.GestureState.GestureFinished` or :sip:ref:`~PyQt6.QtCore.Qt.GestureState.GestureCanceled` states.
