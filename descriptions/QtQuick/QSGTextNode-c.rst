.. sip:class-description::
    :status: todo
    :brief: Class for drawing text layouts and text documents in the Qt Quick scene graph
    :digest: 3109f93db0e56d566b13b0fb7372c511

The :sip:ref:`~PyQt6.QtQuick.QSGTextNode` class is a class for drawing text layouts and text documents in the Qt Quick scene graph.

:sip:ref:`~PyQt6.QtQuick.QSGTextNode` can be useful for creating custom Qt Quick items that require text. It is used in Qt Quick by the Text, `TextEdit <https://doc.qt.io/qt-6/qml-qtquick-textedit.html>`_ and `TextInput <https://doc.qt.io/qt-6/qml-qtquick-textinput.html>`_ elements.

You can create :sip:ref:`~PyQt6.QtQuick.QSGTextNode` objects using :sip:ref:`~PyQt6.QtQuick.QQuickWindow.createTextNode`. The :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextLayout` and :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextDocument` functions provide ways to add text to the :sip:ref:`~PyQt6.QtQuick.QSGTextNode`. The text must already be laid out.

**Note:** Properties must be set before :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextLayout` or :sip:ref:`~PyQt6.QtQuick.QSGTextNode.addTextDocument` are called in order to have an effect.

**Note:** The destruction of :sip:ref:`~PyQt6.QtQuick.QSGTextNode` has to be managed with care. In particular, since it references graphics resources, it must be deleted when the Qt Quick scene graph is invalidated. If the node is part of the graph and has the ``OwnedByParent`` flag set (which is the default), this will happen automatically. However, if the ``OwnedByParent`` flag is cleared and the node is disposed of manually, care must be taken to do this when the scene graph is invalidated. This can be done by connecting to the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated` signal, or by implementing a slot in the :sip:ref:`~PyQt6.QtQuick.QQuickItem` subclass which is named ``invalidateSceneGraph()``. See also the documentation of :sip:ref:`~PyQt6.QtQuick.QQuickItem` for more details.
