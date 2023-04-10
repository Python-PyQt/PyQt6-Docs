:orphan:

.. sip:class:: PyQt6.QtOpenGLWidgets.QOpenGLWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtOpenGLWidgets/QOpenGLWidget-c.rst

    .. sip:enum:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer
        :description: QtOpenGLWidgets/QOpenGLWidget-TargetBuffer-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer.LeftBuffer
            :description: QtOpenGLWidgets/QOpenGLWidget-TargetBuffer-LeftBuffer-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer.RightBuffer
            :description: QtOpenGLWidgets/QOpenGLWidget-TargetBuffer-RightBuffer-v.rst

    .. sip:enum:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior
        :description: QtOpenGLWidgets/QOpenGLWidget-UpdateBehavior-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior.NoPartialUpdate
            :description: QtOpenGLWidgets/QOpenGLWidget-UpdateBehavior-NoPartialUpdate-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior.PartialUpdate
            :description: QtOpenGLWidgets/QOpenGLWidget-UpdateBehavior-PartialUpdate-v.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtOpenGLWidgets/QOpenGLWidget-__init__-f-1.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.context
        :returns:
            :sip:ref:`~PyQt6.QtGui.QOpenGLContext`
        :description: QtOpenGLWidgets/QOpenGLWidget-context-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.currentTargetBuffer
        :returns:
            :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer`
        :description: QtOpenGLWidgets/QOpenGLWidget-currentTargetBuffer-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.defaultFramebufferObject
        :returns:
            int
        :description: QtOpenGLWidgets/QOpenGLWidget-defaultFramebufferObject-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.defaultFramebufferObject
        :args:
            :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer`
        :returns:
            int
        :description: QtOpenGLWidgets/QOpenGLWidget-defaultFramebufferObject-f-1.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.doneCurrent
        :description: QtOpenGLWidgets/QOpenGLWidget-doneCurrent-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtOpenGLWidgets/QOpenGLWidget-event-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.format
        :returns:
            :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`
        :description: QtOpenGLWidgets/QOpenGLWidget-format-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.grabFramebuffer
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtOpenGLWidgets/QOpenGLWidget-grabFramebuffer-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.grabFramebuffer
        :args:
            :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtOpenGLWidgets/QOpenGLWidget-grabFramebuffer-f-1.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL
        :description: QtOpenGLWidgets/QOpenGLWidget-initializeGL-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.isValid
        :returns:
            bool
        :description: QtOpenGLWidgets/QOpenGLWidget-isValid-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent
        :description: QtOpenGLWidgets/QOpenGLWidget-makeCurrent-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent
        :args:
            :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer`
        :description: QtOpenGLWidgets/QOpenGLWidget-makeCurrent-f-1.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.metric
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice.PaintDeviceMetric`
        :returns:
            int
        :description: QtOpenGLWidgets/QOpenGLWidget-metric-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintEngine
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPaintEngine`
        :description: QtOpenGLWidgets/QOpenGLWidget-paintEngine-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtOpenGLWidgets/QOpenGLWidget-paintEvent-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL
        :description: QtOpenGLWidgets/QOpenGLWidget-paintGL-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtOpenGLWidgets/QOpenGLWidget-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.resizeGL
        :args:
            int
            int
        :description: QtOpenGLWidgets/QOpenGLWidget-resizeGL-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.setFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`
        :description: QtOpenGLWidgets/QOpenGLWidget-setFormat-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.setTextureFormat
        :args:
            int
        :description: QtOpenGLWidgets/QOpenGLWidget-setTextureFormat-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.setUpdateBehavior
        :args:
            :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior`
        :description: QtOpenGLWidgets/QOpenGLWidget-setUpdateBehavior-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.textureFormat
        :returns:
            int
        :description: QtOpenGLWidgets/QOpenGLWidget-textureFormat-f.rst

    .. sip:method:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.updateBehavior
        :returns:
            :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior`
        :description: QtOpenGLWidgets/QOpenGLWidget-updateBehavior-f.rst

    .. sip:signal:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.aboutToCompose
        :description: QtOpenGLWidgets/QOpenGLWidget-aboutToCompose-s.rst

    .. sip:signal:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.aboutToResize
        :description: QtOpenGLWidgets/QOpenGLWidget-aboutToResize-s.rst

    .. sip:signal:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.frameSwapped
        :description: QtOpenGLWidgets/QOpenGLWidget-frameSwapped-s.rst

    .. sip:signal:: PyQt6.QtOpenGLWidgets.QOpenGLWidget.resized
        :description: QtOpenGLWidgets/QOpenGLWidget-resized-s.rst
