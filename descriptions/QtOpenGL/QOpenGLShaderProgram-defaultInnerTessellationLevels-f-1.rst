.. sip:method-description::
    :status: todo
    :pysig: 78e43d381ff7864fe31ea99d779fe79f
    :realsig: () const
    :digest: 32e5517a1f98639ba42b827883f7b034

Returns the default inner tessellation levels to be used by the tessellation primitive generator in the event that the tessellation control shader does not output them. For more details on OpenGL and Tessellation shaders see `OpenGL Tessellation Shaders <https://doc.qt.io/qt-6/https://www.opengl.org/wiki/Tessellation_Shader>`_.

Returns a QList of floats describing the inner tessellation levels. The vector will always have two elements but not all of them make sense for every mode of tessellation.

**Note:** This returns the global OpenGL state value. It is not specific to this :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` instance.

**Note:** This function is only supported with OpenGL >= 4.0 and will not return valid results with OpenGL ES 3.2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setDefaultInnerTessellationLevels`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.defaultOuterTessellationLevels`.
