.. sip:method-description::
    :status: todo
    :pysig: 252f2463b17d7b65060495677c920d4c
    :realsig: (const QStringList&)
    :digest: 60925071373f67ad26047c313435174b

Sets the list of family names for the font. The names are case insensitive and may include a foundry name. The first family in *families* will be set as the main family for the font.

Each family name entry in *families* may optionally also include a foundry name, e.g. "Helvetica [Cronyx]". If the family is available from more than one foundry and the foundry isn't specified, an arbitrary foundry is chosen. If the family isn't available a family will be set using the :sip:ref:`~PyQt6.QtGui.QFont` algorithm.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.family`, :sip:ref:`~PyQt6.QtGui.QFont.families`, :sip:ref:`~PyQt6.QtGui.QFont.setFamily`, :sip:ref:`~PyQt6.QtGui.QFont.setStyleHint`, :sip:ref:`~PyQt6.QtGui.QFontInfo`.
