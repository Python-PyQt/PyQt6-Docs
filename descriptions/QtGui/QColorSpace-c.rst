.. sip:class-description::
    :status: todo
    :brief: Color space abstraction
    :digest: 2909551ab47f47138b95fd93121a0701

The :sip:ref:`~PyQt6.QtGui.QColorSpace` class provides a color space abstraction.

Color values can be interpreted in different ways, and based on the interpretation can live in different spaces. We call this *color spaces*.

:sip:ref:`~PyQt6.QtGui.QColorSpace` provides access to creating several predefined color spaces and can generate QColorTransforms for converting colors from one color space to another.

:sip:ref:`~PyQt6.QtGui.QColorSpace` can also represent color spaces defined by ICC profiles or embedded in images, that do not otherwise fit the predefined color spaces.

A color space can generally speaking be conceived as a combination of set of primary colors and a transfer function. The primaries defines the axes of the color space, and the transfer function how values are mapped on the axes. The primaries are defined by three primary colors that represent exactly how red, green, and blue look in this particular color space, and a white color that represents where and how bright pure white is. The range of colors expressible by the primary colors is called the gamut, and a color space that can represent a wider range of colors is also known as a wide-gamut color space.

The transfer function or gamma curve determines how each component in the color space is encoded. These are used because human perception does not operate linearly, and the transfer functions try to ensure that colors will seem evenly spaced to human eyes.
