.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: fd6018e729758439898d72ecae1573bc

Sets the style name of the font to *styleName*. When set, other style properties like :sip:ref:`~PyQt6.QtGui.QFont.style` and :sip:ref:`~PyQt6.QtGui.QFont.weight` will be ignored for font matching, though they may be simulated afterwards if supported by the platform's font engine.

Due to the lower quality of artificially simulated styles, and the lack of full cross platform support, it is not recommended to use matching by style name together with matching by style properties

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.styleName`.
