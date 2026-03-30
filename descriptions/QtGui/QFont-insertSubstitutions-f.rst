.. sip:method-description::
    :status: todo
    :pysig: 907292684d18e92e8b3644a00ea8203d
    :realsig: (const QString&, const QStringList&)
    :digest: 149de7416473669da622c806b6a282e6

Inserts the list of families *substituteNames* into the substitution list for *familyName*.

After substituting a font, trigger the updating of the font by destroying and re-creating all :sip:ref:`~PyQt6.QtGui.QFont` objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitution`, :sip:ref:`~PyQt6.QtGui.QFont.removeSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitute`.
