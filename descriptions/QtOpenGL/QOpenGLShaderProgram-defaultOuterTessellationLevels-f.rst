.. sip:method-description::
    :status: todo
    :pysig: 021dbd5510a963cb43170a72ca7d4949
    :realsig: () const
    :digest: 7d5d7bbc0102a28be4bc2815cc075003

Returns the default outer tessellation levels to be used by the tessellation primitive generator in the event that the tessellation control shader does not output them. For more details on OpenGL and Tessellation shaders see `OpenGL Tessellation Shaders <https://doc.qt.io/qt-6/http://www.opengl.org/wiki/Tessellation_Shader>`_.

Returns a QList of floats describing the outer tessellation levels. The vector will always have four elements but not all of them make sense for every mode of tessellation.

**Note:** This returns the global OpenGL state value. It is not specific to this :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` instance.

**Note:** This function is only supported with OpenGL >= 4.0 and will not return valid results with OpenGL ES 3.2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setDefaultOuterTessellationLevels`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.defaultInnerTessellationLevels`.
