.. sip:enum-description::
    :status: todo
    :digest: 2298adedbca49e2bec0363534890c91b

This enum is used by the constructor and :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.setKey`. Its purpose is to enable handling the problem in Unix implementations of semaphores that survive a crash. In Unix, when a semaphore survives a crash, we need a way to force it to reset its resource count, when the system reuses the semaphore. In Windows, where semaphores can't survive a crash, this enum has no effect.
