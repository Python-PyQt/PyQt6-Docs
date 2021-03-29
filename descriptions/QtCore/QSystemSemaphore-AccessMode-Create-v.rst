.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: bd8b32bfa5e57a112cafc7b3e714999b

:sip:ref:`~PyQt6.QtCore.QSystemSemaphore` takes ownership of the semaphore and sets its resource count to the requested value, regardless of whether the semaphore already exists by having survived a crash. This value should be passed to the constructor, when the first semaphore for a particular key is constructed and you know that if the semaphore already exists it could only be because of a crash. In Windows, where a semaphore can't survive a crash, Create and Open have the same behavior.
