.. sip:method-description::
    :status: todo
    :pysig: 0fb6dba9088be54ad0847be3fadcba69
    :realsig: (QSemaphoreReleaser&)
    :digest: 5b6dc7b4badf3426fbfe6684c7bed1ab

Exchanges the responsibilites of ``\*this`` and *other*.

Unlike move assignment, neither of the two objects ever releases its semaphore, if any, as a consequence of swapping.

Therefore this function is very fast and never fails.
