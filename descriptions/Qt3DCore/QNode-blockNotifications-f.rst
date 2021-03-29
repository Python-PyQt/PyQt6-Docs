.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realname: Qt3DCore::QNode::blockNotifications
    :realsig: (bool)
    :digest: 09cc26d6f8875e616b1bb83f0fb1e093

If *block* is ``true``, property change notifications sent by this object to aspects are blocked. If *block* is ``false``, no such blocking will occur.

The return value is the previous value of :sip:ref:`~PyQt6.Qt3DCore.QNode.notificationsBlocked`.

Note that the other notification types will be sent even if the notifications for this object have been blocked.

.. seealso:: :sip:ref:`~PyQt6.Qt3DCore.QNode.notificationsBlocked`.
