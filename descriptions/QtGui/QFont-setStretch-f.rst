.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: cdb833a333158c799889d25f39f37c6d

Sets the stretch factor for the font.

The stretch factor matches a condensed or expanded version of the font or applies a stretch transform that changes the width of all characters in the font by *factor* percent. For example, setting *factor* to 150 results in all characters in the font being 1.5 times (ie. 150%) wider. The minimum stretch factor is 1, and the maximum stretch factor is 4000. The default stretch factor is ``AnyStretch``, which will accept any stretch factor and not apply any transform on the font.

The stretch factor is only applied to outline fonts. The stretch factor is ignored for bitmap fonts.

**Note:** When matching a font with a native non-default stretch factor, requesting a stretch of 100 will stretch it back to a medium width font.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.stretch`, :sip:ref:`~PyQt6.QtGui.QFont.Stretch`.
