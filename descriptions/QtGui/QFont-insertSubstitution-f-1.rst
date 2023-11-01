.. sip:method-description::
    :status: todo
    :pysig: 849d72bf85c319b6643bb7dfd1dcd250
    :realsig: (const QString&, const QString&)
    :digest: 41540c4dee9846b117473097c67311ba

Inserts *substituteName* into the substitution table for the family *familyName*.

After substituting a font, trigger the updating of the font by destroying and re-creating all :sip:ref:`~PyQt6.QtGui.QFont` objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.removeSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitute`, :sip:ref:`~PyQt6.QtGui.QFont.substitutes`.
