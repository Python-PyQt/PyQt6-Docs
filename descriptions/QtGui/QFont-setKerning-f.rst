.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 0016cf5e4d0913b3da5f9eaa604ea261

Enables kerning for this font if *enable* is true; otherwise disables it. By default, kerning is enabled.

When kerning is enabled, glyph metrics do not add up anymore, even for Latin text. In other words, the assumption that width('a') + width('b') is equal to width("ab") is not necessarily true.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.kerning`, :sip:ref:`~PyQt6.QtGui.QFontMetrics`.
