.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d9d606ad3499da83f3e1c1b5fa81a90f

This signal is emitted once the replica is initialized and all property change notifications have been emitted.

It is sometimes useful to respond to property changes as events. For example, you might want to display a user notification when a certain property change occurs. However, this user notification would then also be triggered when a replica first became ``QRemoteObjectReplica::Valid``, as all property change signals are emitted at that time. This isn't always desirable, and ``notified`` allows the developer to distinguish between these two cases.
