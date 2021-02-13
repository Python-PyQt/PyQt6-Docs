.. sip:method-description::
    :status: todo
    :pysig: bc433f34a736713d77fa06b4c6325f0a
    :realsig: (const QString&)
    :digest: caf844b77f8a4c36ef04158da77e4a41

Returns the first family name to be used whenever *familyName* is specified. The lookup is case insensitive.

If there is no substitution for *familyName*, *familyName* is returned.

To obtain a list of substitutions use :sip:ref:`~PyQt6.QtGui.QFont.substitutes`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.setFamily`, :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitution`, :sip:ref:`~PyQt6.QtGui.QFont.removeSubstitutions`.
