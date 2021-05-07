.. sip:class-description::
    :status: todo
    :brief: General information about fonts
    :digest: 3e3301ac70b6274879974382acea56ae

The :sip:ref:`~PyQt6.QtGui.QFontInfo` class provides general information about fonts.

The :sip:ref:`~PyQt6.QtGui.QFontInfo` class provides the same access functions as :sip:ref:`~PyQt6.QtGui.QFont`, e.g. :sip:ref:`~PyQt6.QtGui.QFontInfo.family`, :sip:ref:`~PyQt6.QtGui.QFontInfo.pointSize`, :sip:ref:`~PyQt6.QtGui.QFontInfo.italic`, :sip:ref:`~PyQt6.QtGui.QFontInfo.weight`, :sip:ref:`~PyQt6.QtGui.QFontInfo.fixedPitch`, :sip:ref:`~PyQt6.QtGui.QFontInfo.styleHint` etc. But whilst the :sip:ref:`~PyQt6.QtGui.QFont` access functions return the values that were set, a :sip:ref:`~PyQt6.QtGui.QFontInfo` object returns the values that apply to the font that will actually be used to draw the text.

For example, when the program asks for a 25pt Courier font on a machine that has a non-scalable 24pt Courier font, :sip:ref:`~PyQt6.QtGui.QFont` will (normally) use the 24pt Courier for rendering. In this case, :sip:ref:`~PyQt6.QtGui.QFont.pointSize` returns 25 and :sip:ref:`~PyQt6.QtGui.QFontInfo.pointSize` returns 24.

There are three ways to create a :sip:ref:`~PyQt6.QtGui.QFontInfo` object.

#. Calling the :sip:ref:`~PyQt6.QtGui.QFontInfo` constructor with a :sip:ref:`~PyQt6.QtGui.QFont` creates a font info object for a screen-compatible font, i.e. the font cannot be a printer font. If the font is changed later, the font info object is *not* updated.

   (Note: If you use a printer font the values returned may be inaccurate. Printer fonts are not always accessible so the nearest screen font is used if a printer font is supplied.)

#. :sip:ref:`~PyQt6.QtWidgets.QWidget.fontInfo` returns the font info for a widget's font. This is equivalent to calling :sip:ref:`~PyQt6.QtGui.QFontInfo`\ (widget->font()). If the widget's font is changed later, the font info object is *not* updated.

#. :sip:ref:`~PyQt6.QtGui.QPainter.fontInfo` returns the font info for a painter's current font. If the painter's font is changed later, the font info object is *not* updated.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont`, :sip:ref:`~PyQt6.QtGui.QFontMetrics`, :sip:ref:`~PyQt6.QtGui.QFontDatabase`.
