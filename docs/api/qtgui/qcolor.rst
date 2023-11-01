:orphan:

.. sip:class:: PyQt6.QtGui.QColor
    :description: QtGui/QColor-c.rst

    .. sip:enum:: PyQt6.QtGui.QColor.NameFormat
        :description: QtGui/QColor-NameFormat-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.NameFormat.HexArgb
            :description: QtGui/QColor-NameFormat-HexArgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.NameFormat.HexRgb
            :description: QtGui/QColor-NameFormat-HexRgb-v.rst

    .. sip:enum:: PyQt6.QtGui.QColor.Spec
        :description: QtGui/QColor-Spec-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.Spec.Cmyk
            :description: QtGui/QColor-Spec-Cmyk-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.Spec.ExtendedRgb
            :description: QtGui/QColor-Spec-ExtendedRgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.Spec.Hsl
            :description: QtGui/QColor-Spec-Hsl-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.Spec.Hsv
            :description: QtGui/QColor-Spec-Hsv-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.Spec.Invalid
            :description: QtGui/QColor-Spec-Invalid-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColor.Spec.Rgb
            :description: QtGui/QColor-Spec-Rgb-v.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :description: QtGui/QColor-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`
        :description: QtGui/QColor-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :args:
            int
        :description: QtGui/QColor-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QRgba64`
        :description: QtGui/QColor-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :args:
            Any
        :description: QtGui/QColor-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :args:
            str
        :description: QtGui/QColor-__init__-f-5.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-__init__-f-6.rst

    .. sip:method:: PyQt6.QtGui.QColor.__init__
        :args:
            int
            int
            int
            alpha: int = 255
        :description: QtGui/QColor-__init__-f-7.rst

    .. sip:method:: PyQt6.QtGui.QColor.alpha
        :returns:
            int
        :description: QtGui/QColor-alpha-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.alphaF
        :returns:
            float
        :description: QtGui/QColor-alphaF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.black
        :returns:
            int
        :description: QtGui/QColor-black-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.blackF
        :returns:
            float
        :description: QtGui/QColor-blackF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.blue
        :returns:
            int
        :description: QtGui/QColor-blue-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.blueF
        :returns:
            float
        :description: QtGui/QColor-blueF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.colorNames
        :returns:
            List[str]
        :static:
        :description: QtGui/QColor-colorNames-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.convertTo
        :args:
            :sip:ref:`~PyQt6.QtGui.QColor.Spec`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-convertTo-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.cyan
        :returns:
            int
        :description: QtGui/QColor-cyan-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.cyanF
        :returns:
            float
        :description: QtGui/QColor-cyanF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.darker
        :args:
            factor: int = 200
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-darker-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.__eq__
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :returns:
            bool
        :description: QtGui/QColor-__eq__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromCmyk
        :args:
            int
            int
            int
            int
            alpha: int = 255
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromCmyk-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromCmykF
        :args:
            float
            float
            float
            float
            alpha: float = 1
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromCmykF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromHsl
        :args:
            int
            int
            int
            alpha: int = 255
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromHsl-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromHslF
        :args:
            float
            float
            float
            alpha: float = 1
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromHslF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromHsv
        :args:
            int
            int
            int
            alpha: int = 255
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromHsv-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromHsvF
        :args:
            float
            float
            float
            alpha: float = 1
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromHsvF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromRgb
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromRgb-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromRgb
        :args:
            int
            int
            int
            alpha: int = 255
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromRgb-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromRgba
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromRgba-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromRgba64
        :args:
            :sip:ref:`~PyQt6.QtGui.QRgba64`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromRgba64-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromRgba64
        :args:
            int
            int
            int
            alpha: int = USHRT_MAX
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromRgba64-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromRgbF
        :args:
            float
            float
            float
            alpha: float = 1
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromRgbF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.fromString
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :static:
        :description: QtGui/QColor-fromString-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.getCmyk
        :returns:
            int
            int
            int
            int
            int
        :description: QtGui/QColor-getCmyk-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.getCmykF
        :returns:
            float
            float
            float
            float
            float
        :description: QtGui/QColor-getCmykF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.getHsl
        :returns:
            int
            int
            int
            int
        :description: QtGui/QColor-getHsl-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.getHslF
        :returns:
            float
            float
            float
            float
        :description: QtGui/QColor-getHslF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.getHsv
        :returns:
            int
            int
            int
            int
        :description: QtGui/QColor-getHsv-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.getHsvF
        :returns:
            float
            float
            float
            float
        :description: QtGui/QColor-getHsvF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.getRgb
        :returns:
            int
            int
            int
            int
        :description: QtGui/QColor-getRgb-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.getRgbF
        :returns:
            float
            float
            float
            float
        :description: QtGui/QColor-getRgbF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.green
        :returns:
            int
        :description: QtGui/QColor-green-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.greenF
        :returns:
            float
        :description: QtGui/QColor-greenF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hslHue
        :returns:
            int
        :description: QtGui/QColor-hslHue-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hslHueF
        :returns:
            float
        :description: QtGui/QColor-hslHueF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hslSaturation
        :returns:
            int
        :description: QtGui/QColor-hslSaturation-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hslSaturationF
        :returns:
            float
        :description: QtGui/QColor-hslSaturationF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hsvHue
        :returns:
            int
        :description: QtGui/QColor-hsvHue-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hsvHueF
        :returns:
            float
        :description: QtGui/QColor-hsvHueF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hsvSaturation
        :returns:
            int
        :description: QtGui/QColor-hsvSaturation-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hsvSaturationF
        :returns:
            float
        :description: QtGui/QColor-hsvSaturationF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hue
        :returns:
            int
        :description: QtGui/QColor-hue-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.hueF
        :returns:
            float
        :description: QtGui/QColor-hueF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.isValid
        :returns:
            bool
        :description: QtGui/QColor-isValid-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.isValidColor
        :args:
            Optional[str]
        :returns:
            bool
        :static:
        :description: QtGui/QColor-isValidColor-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.isValidColorName
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :returns:
            bool
        :static:
        :description: QtGui/QColor-isValidColorName-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.lighter
        :args:
            factor: int = 150
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-lighter-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.lightness
        :returns:
            int
        :description: QtGui/QColor-lightness-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.lightnessF
        :returns:
            float
        :description: QtGui/QColor-lightnessF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.magenta
        :returns:
            int
        :description: QtGui/QColor-magenta-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.magentaF
        :returns:
            float
        :description: QtGui/QColor-magentaF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.name
        :args:
            format: :sip:ref:`~PyQt6.QtGui.QColor.NameFormat` = :sip:ref:`~PyQt6.QtGui.QColor.NameFormat.HexRgb`
        :returns:
            str
        :description: QtGui/QColor-name-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.__ne__
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :returns:
            bool
        :description: QtGui/QColor-__ne__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.red
        :returns:
            int
        :description: QtGui/QColor-red-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.redF
        :returns:
            float
        :description: QtGui/QColor-redF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.rgb
        :returns:
            int
        :description: QtGui/QColor-rgb-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.rgba
        :returns:
            int
        :description: QtGui/QColor-rgba-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.rgba64
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRgba64`
        :description: QtGui/QColor-rgba64-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.saturation
        :returns:
            int
        :description: QtGui/QColor-saturation-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.saturationF
        :returns:
            float
        :description: QtGui/QColor-saturationF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setAlpha
        :args:
            int
        :description: QtGui/QColor-setAlpha-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setAlphaF
        :args:
            float
        :description: QtGui/QColor-setAlphaF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setBlue
        :args:
            int
        :description: QtGui/QColor-setBlue-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setBlueF
        :args:
            float
        :description: QtGui/QColor-setBlueF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setCmyk
        :args:
            int
            int
            int
            int
            alpha: int = 255
        :description: QtGui/QColor-setCmyk-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setCmykF
        :args:
            float
            float
            float
            float
            alpha: float = 1
        :description: QtGui/QColor-setCmykF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setGreen
        :args:
            int
        :description: QtGui/QColor-setGreen-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setGreenF
        :args:
            float
        :description: QtGui/QColor-setGreenF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setHsl
        :args:
            int
            int
            int
            alpha: int = 255
        :description: QtGui/QColor-setHsl-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setHslF
        :args:
            float
            float
            float
            alpha: float = 1
        :description: QtGui/QColor-setHslF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setHsv
        :args:
            int
            int
            int
            alpha: int = 255
        :description: QtGui/QColor-setHsv-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setHsvF
        :args:
            float
            float
            float
            alpha: float = 1
        :description: QtGui/QColor-setHsvF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setNamedColor
        :args:
            str
        :description: QtGui/QColor-setNamedColor-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setRed
        :args:
            int
        :description: QtGui/QColor-setRed-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setRedF
        :args:
            float
        :description: QtGui/QColor-setRedF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setRgb
        :args:
            int
        :description: QtGui/QColor-setRgb-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setRgb
        :args:
            int
            int
            int
            alpha: int = 255
        :description: QtGui/QColor-setRgb-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColor.setRgba
        :args:
            int
        :description: QtGui/QColor-setRgba-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setRgba64
        :args:
            :sip:ref:`~PyQt6.QtGui.QRgba64`
        :description: QtGui/QColor-setRgba64-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.setRgbF
        :args:
            float
            float
            float
            alpha: float = 1
        :description: QtGui/QColor-setRgbF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.spec
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor.Spec`
        :description: QtGui/QColor-spec-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.toCmyk
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-toCmyk-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.toExtendedRgb
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-toExtendedRgb-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.toHsl
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-toHsl-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.toHsv
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-toHsv-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.toRgb
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QColor-toRgb-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.value
        :returns:
            int
        :description: QtGui/QColor-value-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.valueF
        :returns:
            float
        :description: QtGui/QColor-valueF-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.yellow
        :returns:
            int
        :description: QtGui/QColor-yellow-f.rst

    .. sip:method:: PyQt6.QtGui.QColor.yellowF
        :returns:
            float
        :description: QtGui/QColor-yellowF-f.rst
