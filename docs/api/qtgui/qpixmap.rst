:orphan:

.. sip:class:: PyQt6.QtGui.QPixmap
    :inherits: :sip:ref:`~PyQt6.QtGui.QPaintDevice`
    :description: QtGui/QPixmap-c.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.__init__
        :description: QtGui/QPixmap-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QPixmap-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.__init__
        :args:
            List[str]
        :description: QtGui/QPixmap-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.__init__
        :args:
            Any
        :description: QtGui/QPixmap-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.__init__
        :args:
            int
            int
        :description: QtGui/QPixmap-__init__-f-5.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.__init__
        :args:
            str
            format: str = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag` = :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor`
        :description: QtGui/QPixmap-__init__-f-7.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.cacheKey
        :returns:
            int
        :description: QtGui/QPixmap-cacheKey-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.convertFromImage
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
            flags: :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag` = :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor`
        :returns:
            bool
        :description: QtGui/QPixmap-convertFromImage-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.copy
        :args:
            rect: :sip:ref:`~PyQt6.QtCore.QRect` = QRect()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-copy-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.copy
        :args:
            int
            int
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-copy-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.createHeuristicMask
        :args:
            clipTight: bool = True
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBitmap`
        :description: QtGui/QPixmap-createHeuristicMask-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.createMaskFromColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
            mode: :sip:ref:`~PyQt6.QtCore.Qt.MaskMode` = :sip:ref:`~PyQt6.QtCore.Qt.MaskMode.MaskInColor`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBitmap`
        :description: QtGui/QPixmap-createMaskFromColor-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.defaultDepth
        :returns:
            int
        :static:
        :description: QtGui/QPixmap-defaultDepth-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.depth
        :returns:
            int
        :description: QtGui/QPixmap-depth-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.detach
        :description: QtGui/QPixmap-detach-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.deviceIndependentSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtGui/QPixmap-deviceIndependentSize-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.devicePixelRatio
        :returns:
            float
        :description: QtGui/QPixmap-devicePixelRatio-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.devType
        :returns:
            int
        :description: QtGui/QPixmap-devType-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.fill
        :args:
            color: Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int] = :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.white`
        :description: QtGui/QPixmap-fill-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.fromImage
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
            flags: :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag` = :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :static:
        :description: QtGui/QPixmap-fromImage-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.fromImageReader
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageReader`
            flags: :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag` = :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :static:
        :description: QtGui/QPixmap-fromImageReader-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.hasAlpha
        :returns:
            bool
        :description: QtGui/QPixmap-hasAlpha-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.hasAlphaChannel
        :returns:
            bool
        :description: QtGui/QPixmap-hasAlphaChannel-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.height
        :returns:
            int
        :description: QtGui/QPixmap-height-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.isNull
        :returns:
            bool
        :description: QtGui/QPixmap-isNull-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.isQBitmap
        :returns:
            bool
        :description: QtGui/QPixmap-isQBitmap-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.load
        :args:
            str
            format: str = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag` = :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor`
        :returns:
            bool
        :description: QtGui/QPixmap-load-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.loadFromData
        :args:
            bytes
            format: str = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag` = :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor`
        :returns:
            bool
        :description: QtGui/QPixmap-loadFromData-f-2.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.loadFromData
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            format: str = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag` = :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor`
        :returns:
            bool
        :description: QtGui/QPixmap-loadFromData-f-3.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.mask
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBitmap`
        :description: QtGui/QPixmap-mask-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.metric
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice.PaintDeviceMetric`
        :returns:
            int
        :description: QtGui/QPixmap-metric-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.paintEngine
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPaintEngine`
        :description: QtGui/QPixmap-paintEngine-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.rect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QPixmap-rect-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.save
        :args:
            str
            format: str = None
            quality: int = -1
        :returns:
            bool
        :description: QtGui/QPixmap-save-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.save
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            format: str = None
            quality: int = -1
        :returns:
            bool
        :description: QtGui/QPixmap-save-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.scaled
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
            aspectRatioMode: :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode` = :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio`
            transformMode: :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode` = :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.FastTransformation`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-scaled-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.scaled
        :args:
            int
            int
            aspectRatioMode: :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode` = :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio`
            transformMode: :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode` = :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.FastTransformation`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-scaled-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.scaledToHeight
        :args:
            int
            mode: :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode` = :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.FastTransformation`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-scaledToHeight-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.scaledToWidth
        :args:
            int
            mode: :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode` = :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.FastTransformation`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-scaledToWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.scroll
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QRect`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtGui/QPixmap-scroll-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.scroll
        :args:
            int
            int
            int
            int
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtGui/QPixmap-scroll-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.setDevicePixelRatio
        :args:
            float
        :description: QtGui/QPixmap-setDevicePixelRatio-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.setMask
        :args:
            :sip:ref:`~PyQt6.QtGui.QBitmap`
        :description: QtGui/QPixmap-setMask-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.size
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QPixmap-size-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.swap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-swap-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.toImage
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGui/QPixmap-toImage-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.transformed
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
            mode: :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode` = :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.FastTransformation`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QPixmap-transformed-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.trueMatrix
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :static:
        :description: QtGui/QPixmap-trueMatrix-f.rst

    .. sip:method:: PyQt6.QtGui.QPixmap.width
        :returns:
            int
        :description: QtGui/QPixmap-width-f.rst
