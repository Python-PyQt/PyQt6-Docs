.. sip:method-description::
    :status: todo
    :pysig: ffcc31d8a718e8916ca8d006c231bd07
    :realsig: (const QStringList&,int,int,bool)
    :digest: 92f75ff12787a794f32efcca53d943b9

Constructs a font object with the specified *families*, *pointSize*, *weight* and *italic* settings.

If *pointSize* is zero or negative, the point size of the font is set to a system-dependent default value. Generally, this is 12 points.

Each family name entry in *families* may optionally also include a foundry name, e.g. "Helvetica [Cronyx]". If the family is available from more than one foundry and the foundry isn't specified, an arbitrary foundry is chosen. If the family isn't available a family will be set using the :sip:ref:`~PyQt6.QtGui.QFont` algorithm.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.Weight.Weight`, :sip:ref:`~PyQt6.QtGui.QFont.setPointSize`, :sip:ref:`~PyQt6.QtGui.QFont.setWeight`, :sip:ref:`~PyQt6.QtGui.QFont.setItalic`, :sip:ref:`~PyQt6.QtGui.QFont.setStyleHint`, :sip:ref:`~PyQt6.QtGui.QFont.setFamilies`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.font`.
