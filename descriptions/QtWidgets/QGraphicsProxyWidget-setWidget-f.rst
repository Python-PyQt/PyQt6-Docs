.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: fc68f5e539e67712cde1dd40c28eb272

Embeds *widget* into this proxy widget. The embedded widget must reside exclusively either inside or outside of Graphics View. You cannot embed a widget as long as it is is visible elsewhere in the UI, at the same time.

*widget* must be a top-level widget whose parent is ``nullptr``.

When the widget is embedded, its state (e.g., visible, enabled, geometry, size hints) is copied into the proxy widget. If the embedded widget is explicitly hidden or disabled, the proxy widget will become explicitly hidden or disabled after embedding is complete. The class documentation has a full overview over the shared state.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget`'s window flags determine whether the widget, after embedding, will be given window decorations or not.

After this function returns, :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` will keep its state synchronized with that of *widget* whenever possible.

If a widget is already embedded by this proxy when this function is called, that widget will first be automatically unembedded. Passing ``nullptr`` for the *widget* argument will only unembed the widget, and the ownership of the currently embedded widget will be passed on to the caller. Every child widget that are embedded will also be embedded and their proxy widget destroyed.

Note that widgets with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_PaintOnScreen` widget attribute set and widgets that wrap an external application or controller cannot be embedded. Examples are QOpenGLWidget and QAxWidget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.widget`.
