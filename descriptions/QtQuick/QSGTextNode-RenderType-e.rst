.. sip:enum-description::
    :status: todo
    :digest: ab9d493412a6f1fa3588a3364848ef93

This enum type describes type of glyph node used for rendering the text.

Select ``NativeRendering`` if you prefer text to look native on the target platform and do not require advanced features such as transformation of the text. Using such features in combination with the NativeRendering render type will lend poor and sometimes pixelated results.

Both ``Text.QtRendering`` and ``Text.CurveRendering`` are hardware-accelerated techniques. ``QtRendering`` is the faster of the two, but uses more memory and will exhibit rendering artifacts at large sizes. ``CurveRendering`` should be considered as an alternative in cases where ``QtRendering`` does not give good visual results or where reducing graphics memory consumption is a priority.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGTextNode.setRenderType`, :sip:ref:`~PyQt6.QtQuick.QSGTextNode.setRenderTypeQuality`.
