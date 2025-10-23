.. sip:method-description::
    :status: todo
    :pysig: e4dcfd05e0cd89e64fdcc02c8c0e1cd5
    :realsig: () const
    :digest: 3db796984b0dc6a07563ff65ee585df6

This function should return a mask where each bit represents graphics states changed by the :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` function.

**Note:** With Qt 6 and QRhi-based rendering the only relevant values are :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.StateFlag.ViewportState` and :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.StateFlag.ScissorState`. Other values can be returned but are ignored in practice.

+-------------------+-----------------------------------------------+
| Constant          | Description                                   |
+===================+===============================================+
| ViewportState     | Viewport                                      |
+-------------------+-----------------------------------------------+
| ScissorState      | Scissor test enabled state, scissor rectangle |
+-------------------+-----------------------------------------------+
| DepthState        | This value has no effect in Qt 6.             |
+-------------------+-----------------------------------------------+
| StencilState      | This value has no effect in Qt 6.             |
+-------------------+-----------------------------------------------+
| ColorState        | This value has no effect in Qt 6.             |
+-------------------+-----------------------------------------------+
| BlendState        | This value has no effect in Qt 6.             |
+-------------------+-----------------------------------------------+
| CullState         | This value has no effect in Qt 6.             |
+-------------------+-----------------------------------------------+
| RenderTargetState | This value has no effect in Qt 6.             |
+-------------------+-----------------------------------------------+

**Note:** The ``software`` backend exposes its :sip:ref:`~PyQt6.QtGui.QPainter` and saves and restores before and after invoking :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`. Therefore reporting any changed states from here is not necessary.

The default implementation returns 0, meaning no relevant state was changed in :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.

**Note:** This function may be called before :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.
