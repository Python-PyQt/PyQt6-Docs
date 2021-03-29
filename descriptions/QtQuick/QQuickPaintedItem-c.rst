.. sip:class-description::
    :status: todo
    :brief: Way to use the QPainter API in the QML Scene Graph
    :digest: 892148d08b4ddf31271970c8a322c7b1

The :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem` class provides a way to use the :sip:ref:`~PyQt6.QtGui.QPainter` API in the QML Scene Graph.

The :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem` makes it possible to use the :sip:ref:`~PyQt6.QtGui.QPainter` API with the QML Scene Graph. It sets up a textured rectangle in the Scene Graph and uses a :sip:ref:`~PyQt6.QtGui.QPainter` to paint onto the texture. The render target in Qt 6 is always a :sip:ref:`~PyQt6.QtGui.QImage`. When the render target is a :sip:ref:`~PyQt6.QtGui.QImage`, :sip:ref:`~PyQt6.QtGui.QPainter` first renders into the image then the content is uploaded to the texture. Call :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.update` to trigger a repaint.

To enable :sip:ref:`~PyQt6.QtGui.QPainter` to do anti-aliased rendering, use :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.setAntialiasing`.

To write your own painted item, you first create a subclass of :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem`, and then start by implementing its only pure virtual public function: :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.paint`, which implements the actual painting. The painting will be inside the rectangle spanning from 0,0 to width(),height().

**Note:** It important to understand the performance implications such items can incur. See :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.RenderTarget` and :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.renderTarget`.
