.. sip:method-description::
    :status: todo
    :pysig: 3bd69df0fd7815bae379529dbc083755
    :realsig: (int)
    :digest: fcce985cb0ea5b4cb309d8914e273740

Blocking call that waits for the replica to become initialized or until the *timeout* (in ms) expires. Returns ``true`` if the replica is initialized when the call completes, ``false`` otherwise.

If *timeout* is -1, this function will not time out.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectReplica.isInitialized`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectReplica.initialized`.
