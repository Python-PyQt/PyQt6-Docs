.. sip:method-description::
    :status: todo
    :pysig: 343fbcb7b94aa7ac14600a3f4eb87aee
    :realsig: (QAnyStringView)
    :digest: ac368cb69891d21b92a38aaedbc131b6

Returns an RGB :sip:ref:`~PyQt6.QtGui.QColor` parsed from *name*, which may be in one of these formats:

* #RGB (each of R, G, and B is a single hex digit)

* #RRGGBB

* #AARRGGBB (Since 5.2)

* #RRRGGGBBB

* #RRRRGGGGBBBB

* A name from the list of colors defined in the list of `SVG color keyword names <https://www.w3.org/TR/SVG11/types.html#ColorKeywords>`_ provided by the World Wide Web Consortium; for example, "steelblue" or "gainsboro". These color names work on all platforms. Note that these color names are *not* the same as defined by the :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor` enums, e.g. "green" and :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.green` does not refer to the same color.

* ``transparent`` - representing the absence of a color.

Returns an invalid color if *name* cannot be parsed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.isValidColorName`.
