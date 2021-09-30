:orphan:

.. sip:class:: PyQt6.QtGui.QColorSpace
    :description: QtGui/QColorSpace-c.rst

    .. sip:enum:: PyQt6.QtGui.QColorSpace.NamedColorSpace
        :description: QtGui/QColorSpace-NamedColorSpace-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.NamedColorSpace.AdobeRgb
            :description: QtGui/QColorSpace-NamedColorSpace-AdobeRgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.NamedColorSpace.DisplayP3
            :description: QtGui/QColorSpace-NamedColorSpace-DisplayP3-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.NamedColorSpace.ProPhotoRgb
            :description: QtGui/QColorSpace-NamedColorSpace-ProPhotoRgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.NamedColorSpace.SRgb
            :description: QtGui/QColorSpace-NamedColorSpace-SRgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.NamedColorSpace.SRgbLinear
            :description: QtGui/QColorSpace-NamedColorSpace-SRgbLinear-v.rst

    .. sip:enum:: PyQt6.QtGui.QColorSpace.Primaries
        :description: QtGui/QColorSpace-Primaries-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.Primaries.AdobeRgb
            :description: QtGui/QColorSpace-Primaries-AdobeRgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.Primaries.Custom
            :description: QtGui/QColorSpace-Primaries-Custom-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.Primaries.DciP3D65
            :description: QtGui/QColorSpace-Primaries-DciP3D65-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.Primaries.ProPhotoRgb
            :description: QtGui/QColorSpace-Primaries-ProPhotoRgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.Primaries.SRgb
            :description: QtGui/QColorSpace-Primaries-SRgb-v.rst

    .. sip:enum:: PyQt6.QtGui.QColorSpace.TransferFunction
        :description: QtGui/QColorSpace-TransferFunction-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.TransferFunction.Custom
            :description: QtGui/QColorSpace-TransferFunction-Custom-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.TransferFunction.Gamma
            :description: QtGui/QColorSpace-TransferFunction-Gamma-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.TransferFunction.Linear
            :description: QtGui/QColorSpace-TransferFunction-Linear-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.TransferFunction.ProPhotoRgb
            :description: QtGui/QColorSpace-TransferFunction-ProPhotoRgb-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QColorSpace.TransferFunction.SRgb
            :description: QtGui/QColorSpace-TransferFunction-SRgb-v.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :description: QtGui/QColorSpace-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.NamedColorSpace`
        :description: QtGui/QColorSpace-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :description: QtGui/QColorSpace-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.Primaries`
            float
        :description: QtGui/QColorSpace-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.Primaries`
            Iterable[int]
        :description: QtGui/QColorSpace-__init__-f-6.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.Primaries`
            :sip:ref:`~PyQt6.QtGui.QColorSpace.TransferFunction`
            gamma: float = 0
        :description: QtGui/QColorSpace-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            Iterable[int]
        :description: QtGui/QColorSpace-__init__-f-7.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtGui.QColorSpace.TransferFunction`
            gamma: float = 0
        :description: QtGui/QColorSpace-__init__-f-5.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            Iterable[int]
            Iterable[int]
            Iterable[int]
        :description: QtGui/QColorSpace-__init__-f-8.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.description
        :returns:
            str
        :description: QtGui/QColorSpace-description-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :returns:
            bool
        :description: QtGui/QColorSpace-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.fromIccProfile
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :static:
        :description: QtGui/QColorSpace-fromIccProfile-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.gamma
        :returns:
            float
        :description: QtGui/QColorSpace-gamma-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.iccProfile
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QColorSpace-iccProfile-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.isValid
        :returns:
            bool
        :description: QtGui/QColorSpace-isValid-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :returns:
            bool
        :description: QtGui/QColorSpace-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.primaries
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.Primaries`
        :description: QtGui/QColorSpace-primaries-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.setDescription
        :args:
            str
        :description: QtGui/QColorSpace-setDescription-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.setPrimaries
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.Primaries`
        :description: QtGui/QColorSpace-setPrimaries-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.setPrimaries
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QColorSpace-setPrimaries-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.setTransferFunction
        :args:
            Iterable[int]
        :description: QtGui/QColorSpace-setTransferFunction-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.setTransferFunction
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.TransferFunction`
            gamma: float = 0
        :description: QtGui/QColorSpace-setTransferFunction-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.setTransferFunctions
        :args:
            Iterable[int]
            Iterable[int]
            Iterable[int]
        :description: QtGui/QColorSpace-setTransferFunctions-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.swap
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :description: QtGui/QColorSpace-swap-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.transferFunction
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.TransferFunction`
        :description: QtGui/QColorSpace-transferFunction-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.transformationToColorSpace
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColorTransform`
        :description: QtGui/QColorSpace-transformationToColorSpace-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.withTransferFunction
        :args:
            Iterable[int]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :description: QtGui/QColorSpace-withTransferFunction-f-1.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.withTransferFunction
        :args:
            :sip:ref:`~PyQt6.QtGui.QColorSpace.TransferFunction`
            gamma: float = 0
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :description: QtGui/QColorSpace-withTransferFunction-f.rst

    .. sip:method:: PyQt6.QtGui.QColorSpace.withTransferFunctions
        :args:
            Iterable[int]
            Iterable[int]
            Iterable[int]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColorSpace`
        :description: QtGui/QColorSpace-withTransferFunctions-f.rst
