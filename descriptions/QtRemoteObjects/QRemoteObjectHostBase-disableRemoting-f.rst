.. sip:method-description::
    :status: todo
    :pysig: d0e666a5ec41c69d231329e4609ff9c0
    :realsig: (QObject*)
    :digest: 90eaa8be92c2661bceeb439cab78782c

Disables remote access for the :sip:ref:`~PyQt6.QtCore.QObject` *remoteObject*. Returns ``false`` if the current node is a client node or if the *remoteObject* is not registered, and returns ``true`` if remoting is successfully disabled for the Source object.

**Warning:** Replicas of this object will no longer be valid after calling this method.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.enableRemoting`.
