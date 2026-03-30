.. sip:method-description::
    :status: todo
    :pysig: 23007ca189a751a4732ef7fca8222903
    :realsig: (const QString&, const QString&)
    :digest: 868384cd22f979f6c9f7a8e4993d25fe

Returns ``true`` if the font that has family *family* and style *style* is smoothly scalable; otherwise returns ``false``. If this function returns ``true``, it's safe to scale this font to any size, and the result will always look attractive.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.isScalable`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.isBitmapScalable`.
