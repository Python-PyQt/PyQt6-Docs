.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: da50d38b64e0b04bc194cc9b918d48b8

Sets the stretch factor for the font to *factor*.

The stretch factor changes the width of all characters in the font by factor percent. For example, setting *factor* to 150 results in all characters in the font being 1.5 times (ie. 150%) wider. The default stretch factor is 100. The minimum stretch factor is 1, and the maximum stretch factor is 4000.

The stretch factor is only applied to outline fonts. The stretch factor is ignored for bitmap fonts.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCharFormat.fontStretch`.
