:orphan:

.. sip:class:: PyQt6.QtGui.QTransform
    :description: QtGui/QTransform-c.rst

    .. sip:enum:: PyQt6.QtGui.QTransform.TransformationType
        :description: QtGui/QTransform-TransformationType-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTransform.TransformationType.TxNone
            :description: QtGui/QTransform-TransformationType-TxNone-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTransform.TransformationType.TxProject
            :description: QtGui/QTransform-TransformationType-TxProject-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTransform.TransformationType.TxRotate
            :description: QtGui/QTransform-TransformationType-TxRotate-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTransform.TransformationType.TxScale
            :description: QtGui/QTransform-TransformationType-TxScale-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTransform.TransformationType.TxShear
            :description: QtGui/QTransform-TransformationType-TxShear-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTransform.TransformationType.TxTranslate
            :description: QtGui/QTransform-TransformationType-TxTranslate-v.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__init__
        :description: QtGui/QTransform-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__init__
        :args:
            float
            float
            float
            float
            float
            float
        :description: QtGui/QTransform-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__init__
        :args:
            float
            float
            float
            float
            float
            float
            float
            float
            float
        :description: QtGui/QTransform-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__add__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__add__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.adjoint
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-adjoint-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.determinant
        :returns:
            float
        :description: QtGui/QTransform-determinant-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.dx
        :returns:
            float
        :description: QtGui/QTransform-dx-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.dy
        :returns:
            float
        :description: QtGui/QTransform-dy-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            bool
        :description: QtGui/QTransform-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.fromScale
        :args:
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :static:
        :description: QtGui/QTransform-fromScale-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.fromTranslate
        :args:
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :static:
        :description: QtGui/QTransform-fromTranslate-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__hash__
        :returns:
            int
        :description: QtGui/QTransform-__hash__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__iadd__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__iadd__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__imatmul__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__imatmul__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__imul__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__imul__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__imul__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__imul__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTransform.inverted
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
            bool
        :description: QtGui/QTransform-inverted-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.isAffine
        :returns:
            bool
        :description: QtGui/QTransform-isAffine-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.isIdentity
        :returns:
            bool
        :description: QtGui/QTransform-isIdentity-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.isInvertible
        :returns:
            bool
        :description: QtGui/QTransform-isInvertible-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.isRotating
        :returns:
            bool
        :description: QtGui/QTransform-isRotating-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.isScaling
        :returns:
            bool
        :description: QtGui/QTransform-isScaling-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.isTranslating
        :returns:
            bool
        :description: QtGui/QTransform-isTranslating-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__isub__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__isub__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__itruediv__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__itruediv__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m11
        :returns:
            float
        :description: QtGui/QTransform-m11-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m12
        :returns:
            float
        :description: QtGui/QTransform-m12-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m13
        :returns:
            float
        :description: QtGui/QTransform-m13-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m21
        :returns:
            float
        :description: QtGui/QTransform-m21-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m22
        :returns:
            float
        :description: QtGui/QTransform-m22-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m23
        :returns:
            float
        :description: QtGui/QTransform-m23-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m31
        :returns:
            float
        :description: QtGui/QTransform-m31-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m32
        :returns:
            float
        :description: QtGui/QTransform-m32-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.m33
        :returns:
            float
        :description: QtGui/QTransform-m33-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtGui/QTransform-map-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QTransform-map-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtCore.QLine`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLine`
        :description: QtGui/QTransform-map-f-2.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtCore.QLineF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLineF`
        :description: QtGui/QTransform-map-f-3.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
        :description: QtGui/QTransform-map-f-4.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtGui.QPolygon`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPolygon`
        :description: QtGui/QTransform-map-f-5.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtGui/QTransform-map-f-6.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
        :description: QtGui/QTransform-map-f-7.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            int
            int
        :returns:
            int
            int
        :description: QtGui/QTransform-map-f-8.rst

    .. sip:method:: PyQt6.QtGui.QTransform.map
        :args:
            float
            float
        :returns:
            float
            float
        :description: QtGui/QTransform-map-f-9.rst

    .. sip:method:: PyQt6.QtGui.QTransform.mapRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QTransform-mapRect-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.mapRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QTransform-mapRect-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTransform.mapToPolygon
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPolygon`
        :description: QtGui/QTransform-mapToPolygon-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__matmul__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__matmul__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__mul__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__mul__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__mul__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__mul__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            bool
        :description: QtGui/QTransform-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.quadToQuad
        :args:
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            bool
        :static:
        :description: QtGui/QTransform-quadToQuad-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.quadToSquare
        :args:
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            bool
        :static:
        :description: QtGui/QTransform-quadToSquare-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.reset
        :description: QtGui/QTransform-reset-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.rotate
        :args:
            float
            axis: :sip:ref:`~PyQt6.QtCore.Qt.Axis` = :sip:ref:`~PyQt6.QtCore.Qt.Axis.ZAxis`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-rotate-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.rotateRadians
        :args:
            float
            axis: :sip:ref:`~PyQt6.QtCore.Qt.Axis` = :sip:ref:`~PyQt6.QtCore.Qt.Axis.ZAxis`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-rotateRadians-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.scale
        :args:
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-scale-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.setMatrix
        :args:
            float
            float
            float
            float
            float
            float
            float
            float
            float
        :description: QtGui/QTransform-setMatrix-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.shear
        :args:
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-shear-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.squareToQuad
        :args:
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            bool
        :static:
        :description: QtGui/QTransform-squareToQuad-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__sub__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__sub__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.translate
        :args:
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-translate-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.transposed
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-transposed-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.__truediv__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtGui/QTransform-__truediv__-f.rst

    .. sip:method:: PyQt6.QtGui.QTransform.type
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTransform.TransformationType`
        :description: QtGui/QTransform-type-f.rst
