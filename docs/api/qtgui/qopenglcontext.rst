:orphan:

.. sip:class:: PyQt6.QtGui.QOpenGLContext
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QOpenGLContext-c.rst

    .. sip:enum:: PyQt6.QtGui.QOpenGLContext.OpenGLModuleType
        :description: QtGui/QOpenGLContext-OpenGLModuleType-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QOpenGLContext.OpenGLModuleType.LibGL
            :description: QtGui/QOpenGLContext-OpenGLModuleType-LibGL-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QOpenGLContext.OpenGLModuleType.LibGLES
            :description: QtGui/QOpenGLContext-OpenGLModuleType-LibGLES-v.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QOpenGLContext-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.areSharing
        :args:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :returns:
            bool
        :static:
        :description: QtGui/QOpenGLContext-areSharing-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.create
        :returns:
            bool
        :description: QtGui/QOpenGLContext-create-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.currentContext
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :static:
        :description: QtGui/QOpenGLContext-currentContext-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.defaultFramebufferObject
        :returns:
            int
        :description: QtGui/QOpenGLContext-defaultFramebufferObject-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.doneCurrent
        :description: QtGui/QOpenGLContext-doneCurrent-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.extensions
        :returns:
            Set[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtGui/QOpenGLContext-extensions-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.format
        :returns:
            :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`
        :description: QtGui/QOpenGLContext-format-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.getProcAddress
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtGui/QOpenGLContext-getProcAddress-f-2.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.globalShareContext
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :static:
        :description: QtGui/QOpenGLContext-globalShareContext-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.hasExtension
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtGui/QOpenGLContext-hasExtension-f-1.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.isOpenGLES
        :returns:
            bool
        :description: QtGui/QOpenGLContext-isOpenGLES-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.isValid
        :returns:
            bool
        :description: QtGui/QOpenGLContext-isValid-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.makeCurrent
        :args:
            :sip:ref:`~PyQt6.QtGui.QSurface`
        :returns:
            bool
        :description: QtGui/QOpenGLContext-makeCurrent-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.openGLModuleType
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext.OpenGLModuleType`
        :static:
        :description: QtGui/QOpenGLContext-openGLModuleType-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.screen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtGui/QOpenGLContext-screen-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.setFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`
        :description: QtGui/QOpenGLContext-setFormat-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.setScreen
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtGui/QOpenGLContext-setScreen-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.setShareContext
        :args:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :description: QtGui/QOpenGLContext-setShareContext-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.shareContext
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :description: QtGui/QOpenGLContext-shareContext-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.shareGroup
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContextGroup`
        :description: QtGui/QOpenGLContext-shareGroup-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.supportsThreadedOpenGL
        :returns:
            bool
        :static:
        :description: QtGui/QOpenGLContext-supportsThreadedOpenGL-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.surface
        :returns:
            :sip:ref:`~PyQt6.QtGui.QSurface`
        :description: QtGui/QOpenGLContext-surface-f.rst

    .. sip:method:: PyQt6.QtGui.QOpenGLContext.swapBuffers
        :args:
            :sip:ref:`~PyQt6.QtGui.QSurface`
        :description: QtGui/QOpenGLContext-swapBuffers-f.rst

    .. sip:signal:: PyQt6.QtGui.QOpenGLContext.aboutToBeDestroyed
        :description: QtGui/QOpenGLContext-aboutToBeDestroyed-s.rst
