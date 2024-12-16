.. sip:class-description::
    :status: todo
    :brief: Transformation between color spaces
    :digest: 69811de8528f870180ddccfcb41bb2d1

The :sip:ref:`~PyQt6.QtGui.QColorTransform` class is a transformation between color spaces.

:sip:ref:`~PyQt6.QtGui.QColorTransform` is an instantiation of a transformation between color spaces. It can be applied on color and pixels to convert them from one color space to another.

To create a :sip:ref:`~PyQt6.QtGui.QColorTransform`, use :sip:ref:`~PyQt6.QtGui.QColorSpace.transformationToColorSpace`:

::

    QColorSpace sourceColorSpace(QColorSpace::SRgb);
    QColorSpace targetColorSpace(QColorSpace::DisplayP3);
    QColorTransform srgbToP3Transform = sourceColorSpace.transformationToColorSpace(targetColorSpace);

Setting up a :sip:ref:`~PyQt6.QtGui.QColorTransform` takes some preprocessing, so keeping around QColorTransforms that you need often is recommended, instead of generating them on the fly.
