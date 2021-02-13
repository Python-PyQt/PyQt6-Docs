.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 60925071373f67ad26047c313435174b

Sets the list of family names for the font. The names are case insensitive and may include a foundry name. The first family in *families* will be set as the main family for the font.

Each family name entry in *families* may optionally also include a foundry name, e.g. "Helvetica [Cronyx]". If the family is available from more than one foundry and the foundry isn't specified, an arbitrary foundry is chosen. If the family isn't available a family will be set using the `font matching <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ algorithm.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.family`, :sip:ref:`~PyQt6.QtGui.QFont.families`, :sip:ref:`~PyQt6.QtGui.QFont.setFamily`, :sip:ref:`~PyQt6.QtGui.QFont.setStyleHint`, :sip:ref:`~PyQt6.QtGui.QFontInfo`.
