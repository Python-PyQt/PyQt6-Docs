:orphan:

.. sip:class:: PyQt6.QtMultimedia.QVideoFrame
    :description: QtMultimedia/QVideoFrame-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QVideoFrame.HandleType
        :description: QtMultimedia/QVideoFrame-HandleType-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.HandleType.NoHandle
            :description: QtMultimedia/QVideoFrame-HandleType-NoHandle-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.HandleType.RhiTextureHandle
            :description: QtMultimedia/QVideoFrame-HandleType-RhiTextureHandle-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QVideoFrame.MapMode
        :description: QtMultimedia/QVideoFrame-MapMode-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.MapMode.NotMapped
            :description: QtMultimedia/QVideoFrame-MapMode-NotMapped-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.MapMode.ReadOnly
            :description: QtMultimedia/QVideoFrame-MapMode-ReadOnly-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.MapMode.ReadWrite
            :description: QtMultimedia/QVideoFrame-MapMode-ReadWrite-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.MapMode.WriteOnly
            :description: QtMultimedia/QVideoFrame-MapMode-WriteOnly-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QVideoFrame.RotationAngle
        :description: QtMultimedia/QVideoFrame-RotationAngle-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.RotationAngle.Rotation0
            :description: QtMultimedia/QVideoFrame-RotationAngle-Rotation0-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.RotationAngle.Rotation180
            :description: QtMultimedia/QVideoFrame-RotationAngle-Rotation180-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.RotationAngle.Rotation270
            :description: QtMultimedia/QVideoFrame-RotationAngle-Rotation270-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QVideoFrame.RotationAngle.Rotation90
            :description: QtMultimedia/QVideoFrame-RotationAngle-Rotation90-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.__init__
        :description: QtMultimedia/QVideoFrame-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.__init__
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat`
        :description: QtMultimedia/QVideoFrame-__init__-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtMultimedia/QVideoFrame-__init__-f-3.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.__init__
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame`
        :description: QtMultimedia/QVideoFrame-__init__-f-2.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.bits
        :args:
            int
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtMultimedia/QVideoFrame-bits-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.bytesPerLine
        :args:
            int
        :returns:
            int
        :description: QtMultimedia/QVideoFrame-bytesPerLine-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.endTime
        :returns:
            int
        :description: QtMultimedia/QVideoFrame-endTime-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.__eq__
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame`
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-__eq__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.handleType
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.HandleType`
        :description: QtMultimedia/QVideoFrame-handleType-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.height
        :returns:
            int
        :description: QtMultimedia/QVideoFrame-height-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.isMapped
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-isMapped-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.isReadable
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-isReadable-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.isValid
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-isValid-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.isWritable
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-isWritable-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.map
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode`
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-map-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.mapMode
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode`
        :description: QtMultimedia/QVideoFrame-mapMode-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.mappedBytes
        :args:
            int
        :returns:
            int
        :description: QtMultimedia/QVideoFrame-mappedBytes-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.mirrored
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-mirrored-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.__ne__
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame`
        :returns:
            bool
        :description: QtMultimedia/QVideoFrame-__ne__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRectF`
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.PaintOptions`
        :description: QtMultimedia/QVideoFrame-paint-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.pixelFormat
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.PixelFormat`
        :description: QtMultimedia/QVideoFrame-pixelFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.planeCount
        :returns:
            int
        :description: QtMultimedia/QVideoFrame-planeCount-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.rotation
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QtVideo.Rotation`
        :description: QtMultimedia/QVideoFrame-rotation-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.rotationAngle
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.RotationAngle`
        :description: QtMultimedia/QVideoFrame-rotationAngle-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.setEndTime
        :args:
            int
        :description: QtMultimedia/QVideoFrame-setEndTime-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.setMirrored
        :args:
            bool
        :description: QtMultimedia/QVideoFrame-setMirrored-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.setRotation
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QtVideo.Rotation`
        :description: QtMultimedia/QVideoFrame-setRotation-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.setRotationAngle
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.RotationAngle`
        :description: QtMultimedia/QVideoFrame-setRotationAngle-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.setStartTime
        :args:
            int
        :description: QtMultimedia/QVideoFrame-setStartTime-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.setStreamFrameRate
        :args:
            float
        :description: QtMultimedia/QVideoFrame-setStreamFrameRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.setSubtitleText
        :args:
            Optional[str]
        :description: QtMultimedia/QVideoFrame-setSubtitleText-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.size
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtMultimedia/QVideoFrame-size-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.startTime
        :returns:
            int
        :description: QtMultimedia/QVideoFrame-startTime-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.streamFrameRate
        :returns:
            float
        :description: QtMultimedia/QVideoFrame-streamFrameRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.subtitleText
        :returns:
            str
        :description: QtMultimedia/QVideoFrame-subtitleText-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.surfaceFormat
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat`
        :description: QtMultimedia/QVideoFrame-surfaceFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.toImage
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtMultimedia/QVideoFrame-toImage-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.unmap
        :description: QtMultimedia/QVideoFrame-unmap-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QVideoFrame.width
        :returns:
            int
        :description: QtMultimedia/QVideoFrame-width-f.rst
