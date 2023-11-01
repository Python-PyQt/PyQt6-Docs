:orphan:

.. sip:class:: PyQt6.QtGui.QRawFont
    :description: QtGui/QRawFont-c.rst

    .. sip:enum:: PyQt6.QtGui.QRawFont.AntialiasingType
        :description: QtGui/QRawFont-AntialiasingType-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QRawFont.AntialiasingType.PixelAntialiasing
            :description: QtGui/QRawFont-AntialiasingType-PixelAntialiasing-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QRawFont.AntialiasingType.SubPixelAntialiasing
            :description: QtGui/QRawFont-AntialiasingType-SubPixelAntialiasing-v.rst

    .. sip:enum:: PyQt6.QtGui.QRawFont.LayoutFlag
        :description: QtGui/QRawFont-LayoutFlag-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QRawFont.LayoutFlag.KernedAdvances
            :description: QtGui/QRawFont-LayoutFlag-KernedAdvances-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QRawFont.LayoutFlag.SeparateAdvances
            :description: QtGui/QRawFont-LayoutFlag-SeparateAdvances-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QRawFont.LayoutFlag.UseDesignMetrics
            :description: QtGui/QRawFont-LayoutFlag-UseDesignMetrics-v.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.__init__
        :description: QtGui/QRawFont-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QRawFont`
        :description: QtGui/QRawFont-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.__init__
        :args:
            Optional[str]
            float
            hintingPreference: :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference` = :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference.PreferDefaultHinting`
        :description: QtGui/QRawFont-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            float
            hintingPreference: :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference` = :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference.PreferDefaultHinting`
        :description: QtGui/QRawFont-__init__-f-5.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.advancesForGlyphIndexes
        :args:
            Iterable[int]
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QPointF`]
        :description: QtGui/QRawFont-advancesForGlyphIndexes-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.advancesForGlyphIndexes
        :args:
            Iterable[int]
            :sip:ref:`~PyQt6.QtGui.QRawFont.LayoutFlag`
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QPointF`]
        :description: QtGui/QRawFont-advancesForGlyphIndexes-f-2.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.alphaMapForGlyph
        :args:
            int
            antialiasingType: :sip:ref:`~PyQt6.QtGui.QRawFont.AntialiasingType` = :sip:ref:`~PyQt6.QtGui.QRawFont.AntialiasingType.SubPixelAntialiasing`
            transform: :sip:ref:`~PyQt6.QtGui.QTransform` = QTransform()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGui/QRawFont-alphaMapForGlyph-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.ascent
        :returns:
            float
        :description: QtGui/QRawFont-ascent-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.averageCharWidth
        :returns:
            float
        :description: QtGui/QRawFont-averageCharWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.boundingRect
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QRawFont-boundingRect-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.capHeight
        :returns:
            float
        :description: QtGui/QRawFont-capHeight-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.descent
        :returns:
            float
        :description: QtGui/QRawFont-descent-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QRawFont`
        :returns:
            bool
        :description: QtGui/QRawFont-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.familyName
        :returns:
            str
        :description: QtGui/QRawFont-familyName-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.fontTable
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QRawFont-fontTable-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.fromFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
            writingSystem: :sip:ref:`~PyQt6.QtGui.QFontDatabase.WritingSystem` = :sip:ref:`~PyQt6.QtGui.QFontDatabase.WritingSystem.Any`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRawFont`
        :static:
        :description: QtGui/QRawFont-fromFont-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.glyphIndexesForString
        :args:
            Optional[str]
        :returns:
            List[int]
        :description: QtGui/QRawFont-glyphIndexesForString-f-1.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.__hash__
        :returns:
            int
        :description: QtGui/QRawFont-__hash__-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.hintingPreference
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference`
        :description: QtGui/QRawFont-hintingPreference-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.isValid
        :returns:
            bool
        :description: QtGui/QRawFont-isValid-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.leading
        :returns:
            float
        :description: QtGui/QRawFont-leading-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.lineThickness
        :returns:
            float
        :description: QtGui/QRawFont-lineThickness-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.loadFromData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            float
            :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference`
        :description: QtGui/QRawFont-loadFromData-f-1.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.loadFromFile
        :args:
            Optional[str]
            float
            :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference`
        :description: QtGui/QRawFont-loadFromFile-f-1.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.maxCharWidth
        :returns:
            float
        :description: QtGui/QRawFont-maxCharWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QRawFont`
        :returns:
            bool
        :description: QtGui/QRawFont-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.pathForGlyph
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
        :description: QtGui/QRawFont-pathForGlyph-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.pixelSize
        :returns:
            float
        :description: QtGui/QRawFont-pixelSize-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.setPixelSize
        :args:
            float
        :description: QtGui/QRawFont-setPixelSize-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.style
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont.Style`
        :description: QtGui/QRawFont-style-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.styleName
        :returns:
            str
        :description: QtGui/QRawFont-styleName-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.supportedWritingSystems
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QFontDatabase.WritingSystem`]
        :description: QtGui/QRawFont-supportedWritingSystems-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.supportsCharacter
        :args:
            int
        :returns:
            bool
        :description: QtGui/QRawFont-supportsCharacter-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.supportsCharacter
        :args:
            str
        :returns:
            bool
        :description: QtGui/QRawFont-supportsCharacter-f-1.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.swap
        :args:
            :sip:ref:`~PyQt6.QtGui.QRawFont`
        :description: QtGui/QRawFont-swap-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.underlinePosition
        :returns:
            float
        :description: QtGui/QRawFont-underlinePosition-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.unitsPerEm
        :returns:
            float
        :description: QtGui/QRawFont-unitsPerEm-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.weight
        :returns:
            int
        :description: QtGui/QRawFont-weight-f.rst

    .. sip:method:: PyQt6.QtGui.QRawFont.xHeight
        :returns:
            float
        :description: QtGui/QRawFont-xHeight-f.rst
