.. sip:method-description::
    :status: todo
    :pysig: 0b4b82f09673de78985987dd784311ad
    :realsig: (QDeadlineTimer,qint64)
    :digest: 2caa3bb3b8ecc1920c5e7f742288498f

Returns a :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object whose deadline is extended from *dt*'s deadline by *nsecs* nanoseconds. If *dt* was set to never expire, this function returns a :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` that will not expire either.

**Note:** if *dt* was created as expired, its deadline is indeterminate and adding an amount of time may or may not cause it to become unexpired.
