.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ab7d69a29bbf8039807563fcb06daa20

This signal is emitted before the underlying native OpenGL context is destroyed, such that users may clean up OpenGL resources that might otherwise be left dangling in the case of shared OpenGL contexts.

If you wish to make the context current in order to do clean-up, make sure to only connect to the signal using a direct connection.
