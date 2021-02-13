.. sip:method-description::
    :status: todo
    :pysig: 242cbbb0cd71ae47349c0c6a6240d191
    :realsig: (QOpenGLContext*)
    :digest: 5bbc6b4fc94a67ab8e90231849f334dc

Returns ``true`` if shader programs written in the OpenGL Shading Language (GLSL) are supported on this system; false otherwise.

The *context* is used to resolve the GLSL extensions. If *context* is ``nullptr``, then :sip:ref:`~PyQt6.QtGui.QOpenGLContext.currentContext` is used.
