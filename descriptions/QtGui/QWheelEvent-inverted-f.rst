.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 7a31cf3930c19b9840cbd7f8e2964c2d

Returns whether the delta values delivered with the event are inverted.

Normally, a vertical wheel will produce a :sip:ref:`~PyQt6.QtGui.QWheelEvent` with positive delta values if the top of the wheel is rotating away from the hand operating it. Similarly, a horizontal wheel movement will produce a :sip:ref:`~PyQt6.QtGui.QWheelEvent` with positive delta values if the top of the wheel is moved to the left.

However, on some platforms this is configurable, so that the same operations described above will produce negative delta values (but with the same magnitude). With the inverted property a wheel event consumer can choose to always follow the direction of the wheel, regardless of the system settings, but only for specific widgets. (One such use case could be that the user is rotating the wheel in the same direction as a visual Tumbler rotates. Another usecase is to make a slider handle follow the direction of movement of fingers on a touchpad regardless of system configuration.)

**Note:** Many platforms provide no such information. On such platforms inverted always returns false.
