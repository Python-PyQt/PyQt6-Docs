.. sip:enum-description::
    :status: todo
    :digest: db45ea82cc374673e666d62bc5cfb5e4

This enum describes the default render type of text-like elements in Qt Quick (`Text <https://doc.qt.io/qt-6/qml-qtquick-text.html>`_, `TextInput <https://doc.qt.io/qt-6/qml-qtquick-textinput.html>`_, etc.).

Select NativeTextRendering if you prefer text to look native on the target platform and do not require advanced features such as transformation of the text. Using such features in combination with the NativeTextRendering render type will lend poor and sometimes pixelated results.

Both ``QtTextRendering`` and ``CurveTextRendering`` are hardware-accelerated techniques. ``QtTextRendering`` is the faster of the two, but uses more memory and will exhibit rendering artifacts at large sizes. ``CurveTextRendering`` should be considered as an alternative in cases where ``QtTextRendering`` does not give good visual results or where reducing graphics memory consumption is a priority.
