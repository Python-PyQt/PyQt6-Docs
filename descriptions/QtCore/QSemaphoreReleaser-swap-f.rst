.. sip:method-description::
    :status: todo
    :pysig: 0fb6dba9088be54ad0847be3fadcba69
    :realsig: (QSemaphoreReleaser&)
    :digest: e638b071d1cff4b403fc11aa59b339cb

Exchanges the responsibilities of ``\*this`` and *other*.

Unlike move assignment, neither of the two objects ever releases its semaphore, if any, as a consequence of swapping.

Therefore this function is very fast and never fails.
