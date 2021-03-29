.. sip:method-description::
    :status: todo
    :pysig: d87ba2cb29792ba9483f171fe0b46c59
    :realsig: (int)
    :digest: 7e1db63c61c2b50cdc94f888fd5f3102

Waits up to *msecs* milliseconds for all threads to exit and removes all threads from the thread pool. Returns ``true`` if all threads were removed; otherwise it returns ``false``. If *msecs* is -1 (the default), the timeout is ignored (waits for the last thread to exit).
