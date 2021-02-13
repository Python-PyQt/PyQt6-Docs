.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 394496bdcee15a481c4fdaaeddd35326

This signal is emitted when a frame has been queued for presenting. With vertical synchronization enabled the signal is emitted at most once per vsync interval in a continuously animating scene.

This signal will be emitted from the scene graph rendering thread.
