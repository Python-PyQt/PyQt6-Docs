.. sip:method-description::
    :status: todo
    :pysig: 51e8305632b8658a40a1d69eff5afad4
    :realsig: (QFontDatabase::WritingSystem)
    :digest: add200d039b0437fef211b02a3a96eb7

Returns a sorted list of the available font families which support the *writingSystem*.

If a family exists in several foundries, the returned name for that font is in the form "family [foundry]". Examples: "Times [Adobe]", "Times [Cronyx]", "Palatino".

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.writingSystems`.
