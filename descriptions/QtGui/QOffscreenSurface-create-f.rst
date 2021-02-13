.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 4c557767e15393d944aff8beaafeac6f

Allocates the platform resources associated with the offscreen surface.

It is at this point that the surface format set using :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.setFormat` gets resolved into an actual native surface.

Call :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.destroy` to free the platform resources if necessary.

**Note:** Some platforms require this function to be called on the main (GUI) thread.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.destroy`.
