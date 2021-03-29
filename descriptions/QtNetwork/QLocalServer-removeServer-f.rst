.. sip:method-description::
    :status: todo
    :pysig: 787ad3d0f6e2063950bbbf6e050908f3
    :realsig: (const QString&)
    :digest: 738e5deeeaf19688b1b7fe3234ee4b30

Removes any server instance that might cause a call to :sip:ref:`~PyQt6.QtNetwork.QLocalServer.listen` to fail and returns ``true`` if successful; otherwise returns ``false``. This function is meant to recover from a crash, when the previous server instance has not been cleaned up.

On Windows, this function does nothing; on Unix, it removes the socket file given by *name*.

**Warning:** Be careful to avoid removing sockets of running instances.
