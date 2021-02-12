.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: f10aa9664bca0bc0cd49dd80cc6dc089

In this mode, a thread can lock the same :sip:ref:`~PyQt6.QtCore.QReadWriteLock` multiple times. The :sip:ref:`~PyQt6.QtCore.QReadWriteLock` won't be unlocked until a corresponding number of :sip:ref:`~PyQt6.QtCore.QReadWriteLock.unlock` calls have been made.
