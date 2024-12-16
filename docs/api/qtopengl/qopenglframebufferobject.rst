:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLFramebufferObject
    :description: QtOpenGL/QOpenGLFramebufferObject-c.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment
        :description: QtOpenGL/QOpenGLFramebufferObject-Attachment-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment.CombinedDepthStencil
            :description: QtOpenGL/QOpenGLFramebufferObject-Attachment-CombinedDepthStencil-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment.Depth
            :description: QtOpenGL/QOpenGLFramebufferObject-Attachment-Depth-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment.NoAttachment
            :description: QtOpenGL/QOpenGLFramebufferObject-Attachment-NoAttachment-v.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.FramebufferRestorePolicy
        :description: QtOpenGL/QOpenGLFramebufferObject-FramebufferRestorePolicy-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.FramebufferRestorePolicy.DontRestoreFramebufferBinding
            :description: QtOpenGL/QOpenGLFramebufferObject-FramebufferRestorePolicy-DontRestoreFramebufferBinding-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.FramebufferRestorePolicy.RestoreFrameBufferBinding
            :description: QtOpenGL/QOpenGLFramebufferObject-FramebufferRestorePolicy-RestoreFrameBufferBinding-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.FramebufferRestorePolicy.RestoreFramebufferBindingToDefault
            :description: QtOpenGL/QOpenGLFramebufferObject-FramebufferRestorePolicy-RestoreFramebufferBindingToDefault-v.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            target: int = GL_TEXTURE_2D
        :description: QtOpenGL/QOpenGLFramebufferObject-__init__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat`
        :description: QtOpenGL/QOpenGLFramebufferObject-__init__-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.__init__
        :args:
            int
            int
            target: int = GL_TEXTURE_2D
        :description: QtOpenGL/QOpenGLFramebufferObject-__init__-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.__init__
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat`
        :description: QtOpenGL/QOpenGLFramebufferObject-__init__-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment`
            target: int = GL_TEXTURE_2D
            internal_format: int = GL_RGBA8
        :description: QtOpenGL/QOpenGLFramebufferObject-__init__-f-4.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.__init__
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment`
            target: int = GL_TEXTURE_2D
            internal_format: int = GL_RGBA8
        :description: QtOpenGL/QOpenGLFramebufferObject-__init__-f-5.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.addColorAttachment
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            internal_format: int = 0
        :description: QtOpenGL/QOpenGLFramebufferObject-addColorAttachment-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.addColorAttachment
        :args:
            int
            int
            internal_format: int = 0
        :description: QtOpenGL/QOpenGLFramebufferObject-addColorAttachment-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.attachment
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment`
        :description: QtOpenGL/QOpenGLFramebufferObject-attachment-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.bind
        :returns:
            bool
        :description: QtOpenGL/QOpenGLFramebufferObject-bind-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.bindDefault
        :returns:
            bool
        :static:
        :description: QtOpenGL/QOpenGLFramebufferObject-bindDefault-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.blitFramebuffer
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            buffers: int = GL_COLOR_BUFFER_BIT
            filter: int = GL_NEAREST
        :static:
        :description: QtOpenGL/QOpenGLFramebufferObject-blitFramebuffer-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.blitFramebuffer
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            :sip:ref:`~PyQt6.QtCore.QRect`
            buffers: int = GL_COLOR_BUFFER_BIT
            filter: int = GL_NEAREST
        :static:
        :description: QtOpenGL/QOpenGLFramebufferObject-blitFramebuffer-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.blitFramebuffer
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
            int
            int
            int
        :static:
        :description: QtOpenGL/QOpenGLFramebufferObject-blitFramebuffer-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.blitFramebuffer
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject`
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
            int
            int
            int
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.FramebufferRestorePolicy`
        :static:
        :description: QtOpenGL/QOpenGLFramebufferObject-blitFramebuffer-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.format
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat`
        :description: QtOpenGL/QOpenGLFramebufferObject-format-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.handle
        :returns:
            int
        :description: QtOpenGL/QOpenGLFramebufferObject-handle-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.hasOpenGLFramebufferBlit
        :returns:
            bool
        :static:
        :description: QtOpenGL/QOpenGLFramebufferObject-hasOpenGLFramebufferBlit-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.hasOpenGLFramebufferObjects
        :returns:
            bool
        :static:
        :description: QtOpenGL/QOpenGLFramebufferObject-hasOpenGLFramebufferObjects-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.height
        :returns:
            int
        :description: QtOpenGL/QOpenGLFramebufferObject-height-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.isBound
        :returns:
            bool
        :description: QtOpenGL/QOpenGLFramebufferObject-isBound-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.isValid
        :returns:
            bool
        :description: QtOpenGL/QOpenGLFramebufferObject-isValid-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.release
        :returns:
            bool
        :description: QtOpenGL/QOpenGLFramebufferObject-release-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.setAttachment
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.Attachment`
        :description: QtOpenGL/QOpenGLFramebufferObject-setAttachment-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.size
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtOpenGL/QOpenGLFramebufferObject-size-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.sizes
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QSize`]
        :description: QtOpenGL/QOpenGLFramebufferObject-sizes-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.takeTexture
        :returns:
            int
        :description: QtOpenGL/QOpenGLFramebufferObject-takeTexture-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.takeTexture
        :args:
            int
        :returns:
            int
        :description: QtOpenGL/QOpenGLFramebufferObject-takeTexture-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.texture
        :returns:
            int
        :description: QtOpenGL/QOpenGLFramebufferObject-texture-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.textures
        :returns:
            list[int]
        :description: QtOpenGL/QOpenGLFramebufferObject-textures-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.toImage
        :args:
            flipped: bool = True
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtOpenGL/QOpenGLFramebufferObject-toImage-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.toImage
        :args:
            bool
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtOpenGL/QOpenGLFramebufferObject-toImage-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLFramebufferObject.width
        :returns:
            int
        :description: QtOpenGL/QOpenGLFramebufferObject-width-f.rst
