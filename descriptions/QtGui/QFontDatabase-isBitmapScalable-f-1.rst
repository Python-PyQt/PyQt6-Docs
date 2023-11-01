.. sip:method-description::
    :status: todo
    :pysig: 8872bede039115113d9270a9b231a8de
    :realsig: (const QString&, const QString&)
    :digest: 88183ff0006403e7566b1a6773869b44

Returns ``true`` if the font that has family *family* and style *style* is a scalable bitmap font; otherwise returns ``false``. Scaling a bitmap font usually produces an unattractive hardly readable result, because the pixels of the font are scaled. If you need to scale a bitmap font it is better to scale it to one of the fixed sizes returned by :sip:ref:`~PyQt6.QtGui.QFontDatabase.smoothSizes`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.isScalable`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.isSmoothlyScalable`.
