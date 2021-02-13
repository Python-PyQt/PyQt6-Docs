.. sip:method-description::
    :status: todo
    :pysig: bc433f34a736713d77fa06b4c6325f0a
    :realsig: (const QString&,const QString&)
    :digest: 41540c4dee9846b117473097c67311ba

Inserts *substituteName* into the substitution table for the family *familyName*.

After substituting a font, trigger the updating of the font by destroying and re-creating all `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.removeSubstitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitutions`, :sip:ref:`~PyQt6.QtGui.QFont.substitute`, :sip:ref:`~PyQt6.QtGui.QFont.substitutes`.
