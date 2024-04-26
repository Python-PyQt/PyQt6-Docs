.. sip:class-description::
    :status: todo
    :brief: Class for drawing text layouts and text documents in the Qt Quick scene graph
    :digest: d58414ee1ffd5de982bdfa22ecf05ba5

The :sip:ref:`~PyQt6.QtQuick.QSGTextNode` class is a class for drawing text layouts and text documents in the Qt Quick scene graph.

:sip:ref:`~PyQt6.QtQuick.QSGTextNode` can be useful for creating custom Qt Quick items that require text. It is used in Qt Quick by the Text, `TextEdit <https://doc.qt.io/qt-6/qml-qtquick-textedit.html>`_ and `TextInput <https://doc.qt.io/qt-6/qml-qtquick-textinput.html>`_ elements.

You can create :sip:ref:`~PyQt6.QtQuick.QSGTextNode` objects using :sip:ref:`~PyQt6.QtQuick.QQuickWindow.createTextNode`. The :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextLayout` and :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextDocument` functions provide ways to add text to the :sip:ref:`~PyQt6.QtQuick.QSGTextNode`. The text must already be laid out.

**Note:** Properties must be set before :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextLayout` or :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextDocument` are called in order to have an effect.
