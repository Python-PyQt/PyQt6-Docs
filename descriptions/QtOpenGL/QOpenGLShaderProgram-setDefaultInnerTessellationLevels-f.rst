.. sip:method-description::
    :status: todo
    :pysig: 13ab3c5e77307569196120fd7ddfef82
    :realsig: (const QList<float>&)
    :digest: d503656a9edc691b812acebe364f011f

Sets the default outer tessellation levels to be used by the tessellation primitive generator in the event that the tessellation control shader does not output them to *levels*. For more details on OpenGL and Tessellation shaders see `OpenGL Tessellation Shaders <https://doc.qt.io/qt-6/http://www.opengl.org/wiki/Tessellation_Shader>`_.

The *levels* argument should be a QList consisting of 2 floats. Not all of the values make sense for all tessellation modes. If you specify a vector with fewer than 2 elements, the remaining elements will be given a default value of 1.

**Note:** This modifies global OpenGL state and is not specific to this :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` instance. You should call this in your render function when needed, as :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` will not apply this for you. This is purely a convenience function.

**Note:** This function is only available with OpenGL >= 4.0 and is not supported with OpenGL ES 3.2.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.defaultInnerTessellationLevels`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.setDefaultOuterTessellationLevels`.
