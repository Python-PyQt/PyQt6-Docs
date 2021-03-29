.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: (bool)
    :digest: bd5d66e4e808fb7490ba178f75d0860d

*useAlpha* specifies whether to use alpha transparency on newly created windows.

In any application which expects to create translucent windows, it's necessary to set this to true before creating the first :sip:ref:`~PyQt6.QtQuick.QQuickWindow`. The default value is false.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.hasDefaultAlphaBuffer`.
