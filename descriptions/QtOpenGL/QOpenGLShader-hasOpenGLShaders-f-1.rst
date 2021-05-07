.. sip:method-description::
    :status: todo
    :pysig: e67c9d8384cbe50f9f25e96e66f81302
    :realsig: (QOpenGLShader::ShaderType,QOpenGLContext*)
    :digest: d5b701bfd6b121bc13687316c53738c2

Returns ``true`` if shader programs of type *type* are supported on this system; false otherwise.

The *context* is used to resolve the GLSL extensions. If *context* is ``nullptr``, then :sip:ref:`~PyQt6.QtGui.QOpenGLContext.currentContext` is used.
