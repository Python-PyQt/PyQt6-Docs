:orphan:

.. sip:class:: PyQt6.QtGui.QImageIOHandler
    :description: QtGui/QImageIOHandler-c.rst

    .. sip:enum:: PyQt6.QtGui.QImageIOHandler.ImageOption
        :description: QtGui/QImageIOHandler-ImageOption-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.Animation
            :description: QtGui/QImageIOHandler-ImageOption-Animation-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.BackgroundColor
            :description: QtGui/QImageIOHandler-ImageOption-BackgroundColor-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.ClipRect
            :description: QtGui/QImageIOHandler-ImageOption-ClipRect-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.CompressionRatio
            :description: QtGui/QImageIOHandler-ImageOption-CompressionRatio-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.Description
            :description: QtGui/QImageIOHandler-ImageOption-Description-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.Endianness
            :description: QtGui/QImageIOHandler-ImageOption-Endianness-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.Gamma
            :description: QtGui/QImageIOHandler-ImageOption-Gamma-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.ImageTransformation
            :description: QtGui/QImageIOHandler-ImageOption-ImageTransformation-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.IncrementalReading
            :description: QtGui/QImageIOHandler-ImageOption-IncrementalReading-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.Name
            :description: QtGui/QImageIOHandler-ImageOption-Name-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.OptimizedWrite
            :description: QtGui/QImageIOHandler-ImageOption-OptimizedWrite-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.ProgressiveScanWrite
            :description: QtGui/QImageIOHandler-ImageOption-ProgressiveScanWrite-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.Quality
            :description: QtGui/QImageIOHandler-ImageOption-Quality-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.ScaledClipRect
            :description: QtGui/QImageIOHandler-ImageOption-ScaledClipRect-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.ScaledSize
            :description: QtGui/QImageIOHandler-ImageOption-ScaledSize-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.Size
            :description: QtGui/QImageIOHandler-ImageOption-Size-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.SubType
            :description: QtGui/QImageIOHandler-ImageOption-SubType-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.ImageOption.SupportedSubTypes
            :description: QtGui/QImageIOHandler-ImageOption-SupportedSubTypes-v.rst

    .. sip:enum:: PyQt6.QtGui.QImageIOHandler.Transformation
        :description: QtGui/QImageIOHandler-Transformation-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationFlip
            :description: QtGui/QImageIOHandler-Transformation-TransformationFlip-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationFlipAndRotate90
            :description: QtGui/QImageIOHandler-Transformation-TransformationFlipAndRotate90-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationMirror
            :description: QtGui/QImageIOHandler-Transformation-TransformationMirror-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationMirrorAndRotate90
            :description: QtGui/QImageIOHandler-Transformation-TransformationMirrorAndRotate90-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationNone
            :description: QtGui/QImageIOHandler-Transformation-TransformationNone-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationRotate180
            :description: QtGui/QImageIOHandler-Transformation-TransformationRotate180-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationRotate270
            :description: QtGui/QImageIOHandler-Transformation-TransformationRotate270-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageIOHandler.Transformation.TransformationRotate90
            :description: QtGui/QImageIOHandler-Transformation-TransformationRotate90-v.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.__init__
        :description: QtGui/QImageIOHandler-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.canRead
        :returns:
            bool
        :description: QtGui/QImageIOHandler-canRead-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.currentImageNumber
        :returns:
            int
        :description: QtGui/QImageIOHandler-currentImageNumber-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.currentImageRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QImageIOHandler-currentImageRect-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QImageIOHandler-device-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.format
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QImageIOHandler-format-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.imageCount
        :returns:
            int
        :description: QtGui/QImageIOHandler-imageCount-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.jumpToImage
        :args:
            int
        :returns:
            bool
        :description: QtGui/QImageIOHandler-jumpToImage-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.jumpToNextImage
        :returns:
            bool
        :description: QtGui/QImageIOHandler-jumpToNextImage-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.loopCount
        :returns:
            int
        :description: QtGui/QImageIOHandler-loopCount-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.nextImageDelay
        :returns:
            int
        :description: QtGui/QImageIOHandler-nextImageDelay-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.option
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.ImageOption`
        :returns:
            Any
        :description: QtGui/QImageIOHandler-option-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.read
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :returns:
            bool
        :description: QtGui/QImageIOHandler-read-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QImageIOHandler-setDevice-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.setFormat
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtGui/QImageIOHandler-setFormat-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.setOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.ImageOption`
            Any
        :description: QtGui/QImageIOHandler-setOption-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.supportsOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.ImageOption`
        :returns:
            bool
        :description: QtGui/QImageIOHandler-supportsOption-f.rst

    .. sip:method:: PyQt6.QtGui.QImageIOHandler.write
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :returns:
            bool
        :description: QtGui/QImageIOHandler-write-f.rst
