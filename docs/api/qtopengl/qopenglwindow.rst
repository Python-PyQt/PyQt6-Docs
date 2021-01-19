:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLWindow
    :inherits: :sip:ref:`~PyQt6.QtGui.QPaintDeviceWindow`
    :description: QtOpenGL/QOpenGLWindow-c.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior
        :description: QtOpenGL/QOpenGLWindow-UpdateBehavior-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.NoPartialUpdate
            :description: QtOpenGL/QOpenGLWindow-UpdateBehavior-NoPartialUpdate-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.PartialUpdateBlend
            :description: QtOpenGL/QOpenGLWindow-UpdateBehavior-PartialUpdateBlend-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.PartialUpdateBlit
            :description: QtOpenGL/QOpenGLWindow-UpdateBehavior-PartialUpdateBlit-v.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.__init__
        :args:
            updateBehavior: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.NoPartialUpdate`
            parent: :sip:ref:`~PyQt6.QtGui.QWindow` = None
        :description: QtOpenGL/QOpenGLWindow-__init__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
            updateBehavior: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.NoPartialUpdate`
            parent: :sip:ref:`~PyQt6.QtGui.QWindow` = None
        :description: QtOpenGL/QOpenGLWindow-__init__-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.context
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :description: QtOpenGL/QOpenGLWindow-context-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.defaultFramebufferObject
        :returns:
            int
        :description: QtOpenGL/QOpenGLWindow-defaultFramebufferObject-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.doneCurrent
        :description: QtOpenGL/QOpenGLWindow-doneCurrent-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.grabFramebuffer
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtOpenGL/QOpenGLWindow-grabFramebuffer-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.initializeGL
        :description: QtOpenGL/QOpenGLWindow-initializeGL-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.isValid
        :returns:
            bool
        :description: QtOpenGL/QOpenGLWindow-isValid-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.makeCurrent
        :description: QtOpenGL/QOpenGLWindow-makeCurrent-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.metric
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice.PaintDeviceMetric`
        :returns:
            int
        :description: QtOpenGL/QOpenGLWindow-metric-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtOpenGL/QOpenGLWindow-paintEvent-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.paintGL
        :description: QtOpenGL/QOpenGLWindow-paintGL-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.paintOverGL
        :description: QtOpenGL/QOpenGLWindow-paintOverGL-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.paintUnderGL
        :description: QtOpenGL/QOpenGLWindow-paintUnderGL-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtOpenGL/QOpenGLWindow-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.resizeGL
        :args:
            int
            int
        :description: QtOpenGL/QOpenGLWindow-resizeGL-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.shareContext
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :description: QtOpenGL/QOpenGLWindow-shareContext-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLWindow.updateBehavior
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior`
        :description: QtOpenGL/QOpenGLWindow-updateBehavior-f.rst

    .. sip:signal:: PyQt6.QtOpenGL.QOpenGLWindow.frameSwapped
        :description: QtOpenGL/QOpenGLWindow-frameSwapped-s.rst
