.. sip:class-description::
    :status: todo
    :brief: Represents a variable axis in a font
    :digest: 56afd68c6fc08b5d261f5f1386cbec4b

The :sip:ref:`~PyQt6.QtGui.QFontVariableAxis` class represents a variable axis in a font.

Variable fonts provide a way to store multiple variations (with different weights, widths or styles) in the same font file. The variations are given as floating point values for a pre-defined set of parameters, called "variable axes".

Specific parameterizations (sets of values for the axes in a font) can be selected using the properties in :sip:ref:`~PyQt6.QtGui.QFont`, same as with traditional subfamilies that are defined as stand-alone font files. But with variable fonts, arbitrary values can be provided for each axis to gain a fine-grained customization of the font's appearance.

:sip:ref:`~PyQt6.QtGui.QFontVariableAxis` contains information of one axis. Use :sip:ref:`~PyQt6.QtGui.QFontInfo.variableAxes` to retrieve a list of the variable axes defined for a given font. Specific values can be provided for an axis by using :sip:ref:`~PyQt6.QtGui.QFont.setVariableAxis` and passing in the :sip:ref:`~PyQt6.QtGui.QFontVariableAxis.tag`.

**Note:** On Windows, variable axes are not supported if the optional GDI font backend is in use.
