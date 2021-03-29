.. sip:enum-member-description::
    :status: todo
    :value: 19
    :digest: 7d8202fd66737bf4121ff7b19c295c9a

This is the frame rate which should be used while dragging or scrolling. :sip:ref:`~PyQt6.QtWidgets.QScroller` uses a :sip:ref:`~PyQt6.QtCore.QAbstractAnimation` timer internally to sync all scrolling operations to other animations that might be active at the same time. If the standard value of 60 frames per second is too fast, it can be lowered with this setting, while still being in-sync with :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`. Please note that only the values of the :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties.FrameRates.FrameRates` enum are allowed here.
