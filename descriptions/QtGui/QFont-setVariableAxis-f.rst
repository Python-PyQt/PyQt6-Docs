.. sip:method-description::
    :status: todo
    :pysig: 1b2c29769adf6993e211e8c65721063f
    :realsig: (QFont::Tag, float)
    :digest: ce935de800cbbe3aa3b67380657729b3

Applies a *value* to the variable axis corresponding to *tag*.

Variable fonts provide a way to store multiple variations (with different weights, widths or styles) in the same font file. The variations are given as floating point values for a pre-defined set of parameters, called "variable axes". Specific instances are typically given names by the font designer, and, in Qt, these can be selected using :sip:ref:`~PyQt6.QtGui.QFont.setStyleName` just like traditional sub-families.

In some cases, it is also useful to provide arbitrary values for the different axes. For instance, if a font has a Regular and Bold sub-family, you may want a weight in-between these. You could then manually request this by supplying a custom value for the "wght" axis in the font.

::

    QFont font;
    font.setVariableAxis("wght", (QFont::Normal + QFont::Bold) / 2.0f);

If the "wght" axis is supported by the font and the given value is within its defined range, a font corresponding to the weight 550.0 will be provided.

There are a few standard axes than many fonts provide, such as "wght" (weight), "wdth" (width), "ital" (italic) and "opsz" (optical size). They each have indivdual ranges defined in the font itself. For instance, "wght" may span from 100 to 900 (\ :sip:ref:`~PyQt6.QtGui.QFont.Weight.Thin` to :sip:ref:`~PyQt6.QtGui.QFont.Weight.Black`) whereas "ital" can span from 0 to 1 (from not italic to fully italic).

A font may also choose to define custom axes; the only limitation is that the name has to meet the requirements for a :sip:ref:`~PyQt6.QtGui.QFont.Tag` (sequence of four latin-1 characters.)

By default, no variable axes are set.

**Note:** On Windows, variable axes are not supported if the optional GDI font backend is in use.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.unsetVariableAxis`.
