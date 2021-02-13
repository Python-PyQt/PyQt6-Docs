.. sip:method-description::
    :status: todo
    :pysig: b754924ab813f5e3b3453efcce84d25c
    :realsig: (const QString&,const QStringList&)
    :digest: 149de7416473669da622c806b6a282e6

Inserts the list of families *substituteNames* into the substitution list for *familyName*.

After substituting a font, trigger the updating of the font by destroying and re-creating all `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitution`, :sip:ref:`~PyQt6.QtGui.QFont.removeSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitute`.
