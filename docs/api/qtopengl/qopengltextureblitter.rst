:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLTextureBlitter
    :description: QtOpenGL/QOpenGLTextureBlitter-c.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.Origin
        :description: QtOpenGL/QOpenGLTextureBlitter-Origin-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.Origin.OriginBottomLeft
            :description: QtOpenGL/QOpenGLTextureBlitter-Origin-OriginBottomLeft-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.Origin.OriginTopLeft
            :description: QtOpenGL/QOpenGLTextureBlitter-Origin-OriginTopLeft-v.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.__init__
        :description: QtOpenGL/QOpenGLTextureBlitter-__init__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.bind
        :args:
            target: int = GL_TEXTURE_2D
        :description: QtOpenGL/QOpenGLTextureBlitter-bind-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.blit
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.Origin`
        :description: QtOpenGL/QOpenGLTextureBlitter-blit-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.blit
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
            :sip:ref:`~PyQt6.QtGui.QMatrix3x3`
        :description: QtOpenGL/QOpenGLTextureBlitter-blit-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.create
        :returns:
            bool
        :description: QtOpenGL/QOpenGLTextureBlitter-create-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.destroy
        :description: QtOpenGL/QOpenGLTextureBlitter-destroy-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.isCreated
        :returns:
            bool
        :description: QtOpenGL/QOpenGLTextureBlitter-isCreated-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.release
        :description: QtOpenGL/QOpenGLTextureBlitter-release-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.setOpacity
        :args:
            float
        :description: QtOpenGL/QOpenGLTextureBlitter-setOpacity-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.setRedBlueSwizzle
        :args:
            bool
        :description: QtOpenGL/QOpenGLTextureBlitter-setRedBlueSwizzle-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.sourceTransform
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.Origin`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix3x3`
        :static:
        :description: QtOpenGL/QOpenGLTextureBlitter-sourceTransform-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.supportsExternalOESTarget
        :returns:
            bool
        :description: QtOpenGL/QOpenGLTextureBlitter-supportsExternalOESTarget-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLTextureBlitter.targetTransform
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            :sip:ref:`~PyQt6.QtCore.QRect`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :static:
        :description: QtOpenGL/QOpenGLTextureBlitter-targetTransform-f.rst
