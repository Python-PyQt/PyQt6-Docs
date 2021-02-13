.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: cde8a13ceeeca57c6a5fb399954e16b0

This function is used to synchronize the QML scene with the rendering scene graph.

If a dedicated render thread is used, the GUI thread should be blocked for the duration of this call.

Returns *true* if the synchronization changed the scene graph.
