.. sip:method-description::
    :status: todo
    :pysig: de73bee7c95e21348f60101258658424
    :realsig: (QDeadlineTimer)
    :digest: 3fea56f7635cb05f0a7ffc077d046e7d

Waits until *deadline* expires for all threads to exit and removes all threads from the thread pool. Returns ``true`` if all threads were removed; otherwise it returns ``false``.
