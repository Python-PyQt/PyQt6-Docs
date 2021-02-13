.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: c41bdf53770c2bed589afb5c73eb802d

This is the time a mouse press event is delayed when starting a flick gesture in ``[s]``. If the gesture is triggered within that time, no mouse press or release is sent to the scrolled object. If it triggers after that delay the delayed mouse press plus a faked release event at global position ``QPoint(-QWIDGETSIZE_MAX, -QWIDGETSIZE_MAX)`` is sent. If the gesture is canceled, then both the delayed mouse press plus the real release event are delivered.
