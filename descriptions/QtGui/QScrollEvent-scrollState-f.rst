.. sip:method-description::
    :status: todo
    :pysig: b81d8f121a8609f51344925150c1207d
    :realsig: () const
    :digest: 1199c3b73d2f39b6bb6af11c7b2de0bb

Returns the current scroll state as a combination of ScrollStateFlag values. :sip:ref:`~PyQt6.QtGui.QScrollEvent.ScrollState.ScrollStarted` (or :sip:ref:`~PyQt6.QtGui.QScrollEvent.ScrollState.ScrollFinished`) will be set, if this scroll event is the first (or last) event in a scrolling activity. Please note that both values can be set at the same time, if the activity consists of a single :sip:ref:`~PyQt6.QtGui.QScrollEvent`. All other scroll events in between will have their state set to :sip:ref:`~PyQt6.QtGui.QScrollEvent.ScrollState.ScrollUpdated`.

A widget could for example revert selections when scrolling is started and stopped.
