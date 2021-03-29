.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6f50fe0864d90117162e8396e2e32d1b

This signal is emitted on the GUI thread before requesting the render thread to perform the synchronization of the scene graph.

Unlike the other similar signals, this one is emitted on the GUI thread instead of the render thread. It can be used to synchronize external animation systems with the QML content. At the same time this means that this signal is not suitable for triggering graphics operations.
