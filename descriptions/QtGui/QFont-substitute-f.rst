.. sip:method-description::
    :status: todo
    :pysig: 607949925283b263ed00ac5fb0dd5f9d
    :realsig: (const QString&)
    :digest: caf844b77f8a4c36ef04158da77e4a41

Returns the first family name to be used whenever *familyName* is specified. The lookup is case insensitive.

If there is no substitution for *familyName*, *familyName* is returned.

To obtain a list of substitutions use :sip:ref:`~PyQt6.QtGui.QFont.substitutes`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.setFamily`, :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitution`, :sip:ref:`~PyQt6.QtGui.QFont.removeSubstitutions`.
