.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: b4f0212e34d2327fc56107252906fa8d

Same as Qt::QueuedConnection, except that the signalling thread blocks until the slot returns. This connection must *not* be used if the receiver lives in the signalling thread, or else the application will deadlock.
