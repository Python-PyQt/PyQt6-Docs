:orphan:

.. sip:class:: PyQt6.QtQuick.QQuickWindow
    :inherits: :sip:ref:`~PyQt6.QtGui.QWindow`
    :description: QtQuick/QQuickWindow-c.rst

    .. sip:enum:: PyQt6.QtQuick.QQuickWindow.CreateTextureOption
        :description: QtQuick/QQuickWindow-CreateTextureOption-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.CreateTextureOption.TextureCanUseAtlas
            :description: QtQuick/QQuickWindow-CreateTextureOption-TextureCanUseAtlas-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.CreateTextureOption.TextureHasAlphaChannel
            :description: QtQuick/QQuickWindow-CreateTextureOption-TextureHasAlphaChannel-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.CreateTextureOption.TextureHasMipmaps
            :description: QtQuick/QQuickWindow-CreateTextureOption-TextureHasMipmaps-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.CreateTextureOption.TextureIsOpaque
            :description: QtQuick/QQuickWindow-CreateTextureOption-TextureIsOpaque-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.CreateTextureOption.TextureOwnsGLTexture
            :description: QtQuick/QQuickWindow-CreateTextureOption-TextureOwnsGLTexture-v.rst

    .. sip:enum:: PyQt6.QtQuick.QQuickWindow.RenderStage
        :description: QtQuick/QQuickWindow-RenderStage-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.RenderStage.AfterRenderingStage
            :description: QtQuick/QQuickWindow-RenderStage-AfterRenderingStage-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.RenderStage.AfterSwapStage
            :description: QtQuick/QQuickWindow-RenderStage-AfterSwapStage-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.RenderStage.AfterSynchronizingStage
            :description: QtQuick/QQuickWindow-RenderStage-AfterSynchronizingStage-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.RenderStage.BeforeRenderingStage
            :description: QtQuick/QQuickWindow-RenderStage-BeforeRenderingStage-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.RenderStage.BeforeSynchronizingStage
            :description: QtQuick/QQuickWindow-RenderStage-BeforeSynchronizingStage-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.RenderStage.NoStage
            :description: QtQuick/QQuickWindow-RenderStage-NoStage-v.rst

    .. sip:enum:: PyQt6.QtQuick.QQuickWindow.SceneGraphError
        :description: QtQuick/QQuickWindow-SceneGraphError-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.SceneGraphError.ContextNotAvailable
            :description: QtQuick/QQuickWindow-SceneGraphError-ContextNotAvailable-v.rst

    .. sip:enum:: PyQt6.QtQuick.QQuickWindow.TextRenderType
        :description: QtQuick/QQuickWindow-TextRenderType-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.TextRenderType.NativeTextRendering
            :description: QtQuick/QQuickWindow-TextRenderType-NativeTextRendering-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickWindow.TextRenderType.QtTextRendering
            :description: QtQuick/QQuickWindow-TextRenderType-QtTextRendering-v.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtGui.QWindow` = None
        :description: QtQuick/QQuickWindow-__init__-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.activeFocusItem
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickItem`
        :description: QtQuick/QQuickWindow-activeFocusItem-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.beginExternalCommands
        :description: QtQuick/QQuickWindow-beginExternalCommands-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.closeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QCloseEvent`
        :description: QtQuick/QQuickWindow-closeEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.color
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtQuick/QQuickWindow-color-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.contentItem
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickItem`
        :description: QtQuick/QQuickWindow-contentItem-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.createImageNode
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGImageNode`
        :description: QtQuick/QQuickWindow-createImageNode-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.createRectangleNode
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGRectangleNode`
        :description: QtQuick/QQuickWindow-createRectangleNode-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.createTextureFromImage
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGTexture`
        :description: QtQuick/QQuickWindow-createTextureFromImage-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.createTextureFromImage
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
            :sip:ref:`~PyQt6.QtQuick.QQuickWindow.CreateTextureOption`
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGTexture`
        :description: QtQuick/QQuickWindow-createTextureFromImage-f-2.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.effectiveDevicePixelRatio
        :returns:
            float
        :description: QtQuick/QQuickWindow-effectiveDevicePixelRatio-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.endExternalCommands
        :description: QtQuick/QQuickWindow-endExternalCommands-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtQuick/QQuickWindow-event-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.exposeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QExposeEvent`
        :description: QtQuick/QQuickWindow-exposeEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtQuick/QQuickWindow-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.focusObject
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQuick/QQuickWindow-focusObject-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtQuick/QQuickWindow-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.grabWindow
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtQuick/QQuickWindow-grabWindow-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.graphicsApi
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.GraphicsApi`
        :static:
        :description: QtQuick/QQuickWindow-graphicsApi-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.graphicsConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration`
        :description: QtQuick/QQuickWindow-graphicsConfiguration-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.graphicsDevice
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`
        :description: QtQuick/QQuickWindow-graphicsDevice-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.hasDefaultAlphaBuffer
        :returns:
            bool
        :static:
        :description: QtQuick/QQuickWindow-hasDefaultAlphaBuffer-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.hideEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QHideEvent`
        :description: QtQuick/QQuickWindow-hideEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.incubationController
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlIncubationController`
        :description: QtQuick/QQuickWindow-incubationController-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.isPersistentGraphics
        :returns:
            bool
        :description: QtQuick/QQuickWindow-isPersistentGraphics-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.isPersistentSceneGraph
        :returns:
            bool
        :description: QtQuick/QQuickWindow-isPersistentSceneGraph-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.isSceneGraphInitialized
        :returns:
            bool
        :description: QtQuick/QQuickWindow-isSceneGraphInitialized-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtQuick/QQuickWindow-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtQuick/QQuickWindow-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuick/QQuickWindow-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.mouseGrabberItem
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickItem`
        :description: QtQuick/QQuickWindow-mouseGrabberItem-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuick/QQuickWindow-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuick/QQuickWindow-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuick/QQuickWindow-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.releaseResources
        :description: QtQuick/QQuickWindow-releaseResources-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.rendererInterface
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`
        :description: QtQuick/QQuickWindow-rendererInterface-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.renderTarget
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`
        :description: QtQuick/QQuickWindow-renderTarget-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtQuick/QQuickWindow-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.sceneGraphBackend
        :returns:
            str
        :static:
        :description: QtQuick/QQuickWindow-sceneGraphBackend-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.scheduleRenderJob
        :args:
            :sip:ref:`~PyQt6.QtCore.QRunnable`
            :sip:ref:`~PyQt6.QtQuick.QQuickWindow.RenderStage`
        :description: QtQuick/QQuickWindow-scheduleRenderJob-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuick/QQuickWindow-setColor-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setDefaultAlphaBuffer
        :args:
            bool
        :static:
        :description: QtQuick/QQuickWindow-setDefaultAlphaBuffer-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setGraphicsApi
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.GraphicsApi`
        :static:
        :description: QtQuick/QQuickWindow-setGraphicsApi-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setGraphicsConfiguration
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration`
        :description: QtQuick/QQuickWindow-setGraphicsConfiguration-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setGraphicsDevice
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`
        :description: QtQuick/QQuickWindow-setGraphicsDevice-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setPersistentGraphics
        :args:
            bool
        :description: QtQuick/QQuickWindow-setPersistentGraphics-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph
        :args:
            bool
        :description: QtQuick/QQuickWindow-setPersistentSceneGraph-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setRenderTarget
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`
        :description: QtQuick/QQuickWindow-setRenderTarget-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setSceneGraphBackend
        :args:
            Optional[str]
        :static:
        :description: QtQuick/QQuickWindow-setSceneGraphBackend-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.setTextRenderType
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickWindow.TextRenderType`
        :static:
        :description: QtQuick/QQuickWindow-setTextRenderType-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtQuick/QQuickWindow-showEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.tabletEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QTabletEvent`
        :description: QtQuick/QQuickWindow-tabletEvent-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.textRenderType
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickWindow.TextRenderType`
        :static:
        :description: QtQuick/QQuickWindow-textRenderType-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.update
        :description: QtQuick/QQuickWindow-update-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickWindow.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtQuick/QQuickWindow-wheelEvent-f.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.activeFocusItemChanged
        :description: QtQuick/QQuickWindow-activeFocusItemChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.afterAnimating
        :description: QtQuick/QQuickWindow-afterAnimating-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.afterFrameEnd
        :description: QtQuick/QQuickWindow-afterFrameEnd-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.afterRendering
        :description: QtQuick/QQuickWindow-afterRendering-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.afterRenderPassRecording
        :description: QtQuick/QQuickWindow-afterRenderPassRecording-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.afterSynchronizing
        :description: QtQuick/QQuickWindow-afterSynchronizing-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.beforeFrameBegin
        :description: QtQuick/QQuickWindow-beforeFrameBegin-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.beforeRendering
        :description: QtQuick/QQuickWindow-beforeRendering-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.beforeRenderPassRecording
        :description: QtQuick/QQuickWindow-beforeRenderPassRecording-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.beforeSynchronizing
        :description: QtQuick/QQuickWindow-beforeSynchronizing-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.closing
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickCloseEvent`
        :description: QtQuick/QQuickWindow-closing-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.colorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuick/QQuickWindow-colorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.frameSwapped
        :description: QtQuick/QQuickWindow-frameSwapped-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.sceneGraphAboutToStop
        :description: QtQuick/QQuickWindow-sceneGraphAboutToStop-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.sceneGraphError
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickWindow.SceneGraphError`
            Optional[str]
        :description: QtQuick/QQuickWindow-sceneGraphError-s-1.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized
        :description: QtQuick/QQuickWindow-sceneGraphInitialized-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated
        :description: QtQuick/QQuickWindow-sceneGraphInvalidated-s.rst
