.. sip:enum-description::
    :status: todo
    :digest: 8e81e0017e5115480da7d746674f3917

This enum is used by the constructor and setKey(). Its purpose is to enable handling the problem in Unix implementations of semaphores that survive a crash. In Unix, when a semaphore survives a crash, we need a way to force it to reset its resource count, when the system reuses the semaphore. In Windows, where semaphores can't survive a crash, this enum has no effect.
