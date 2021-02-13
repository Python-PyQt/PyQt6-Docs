.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 6e1376caa07fc84c684157e93cafc707

Sets the family name of the font. The name is case insensitive and may include a foundry name.

The *family* name may optionally also include a foundry name, e.g. "Helvetica [Cronyx]". If the *family* is available from more than one foundry and the foundry isn't specified, an arbitrary foundry is chosen. If the family isn't available a family will be set using the `font matching <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ algorithm.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.family`, :sip:ref:`~PyQt6.QtGui.QFont.setStyleHint`, :sip:ref:`~PyQt6.QtGui.QFontInfo`.
