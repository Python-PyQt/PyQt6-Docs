.. sip:method-description::
    :status: todo
    :pysig: 18ecbb7d54d697817f268467fbf3bc85
    :realsig: (QOpenGLContext*)
    :digest: 13907a6e47ad6bf9835e05af214420b8

Returns a new :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice` referencing an existing OpenGL *context*.

This factory function is suitable for OpenGL.

**Note:** It is up the caller to ensure that *context* is going to be compatible and usable with the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`. Platform-specific mismatches in the associated :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`, or threading issues due to attempting to use *context* on multiple threads are up to the caller to avoid.
