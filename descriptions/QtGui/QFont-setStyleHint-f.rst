.. sip:method-description::
    :status: todo
    :pysig: 628768e7267fa5904728f47fd014e2a7
    :realsig: (QFont::StyleHint,QFont::StyleStrategy)
    :digest: f73e4555daacbad86ae115f2717b79bb

Sets the style hint and strategy to *hint* and *strategy*, respectively.

If these aren't set explicitly the style hint will default to ``AnyStyle`` and the style strategy to ``PreferDefault``.

Qt does not support style hints on X11 since this information is not provided by the window system.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.StyleHint.StyleHint`, :sip:ref:`~PyQt6.QtGui.QFont.styleHint`, :sip:ref:`~PyQt6.QtGui.QFont.StyleStrategy.StyleStrategy`, :sip:ref:`~PyQt6.QtGui.QFont.styleStrategy`, :sip:ref:`~PyQt6.QtGui.QFontInfo`.
