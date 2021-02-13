.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 846a8b7ecd5d126c13669d27471a14f3

Sets an arbitrary *widget* as the dock widget's title bar. If *widget* is ``nullptr``, any custom title bar widget previously set on the dock widget is removed, but not deleted, and the default title bar will be used instead.

If a title bar widget is set, :sip:ref:`~PyQt6.QtWidgets.QDockWidget` will not use native window decorations when it is floated.

Here are some tips for implementing custom title bars:

* Mouse events that are not explicitly handled by the title bar widget must be ignored by calling QMouseEvent::ignore(). These events then propagate to the :sip:ref:`~PyQt6.QtWidgets.QDockWidget` parent, which handles them in the usual manner, moving when the title bar is dragged, docking and undocking when it is double-clicked, etc.

* When :sip:ref:`~PyQt6.QtWidgets.QDockWidget.DockWidgetFeatures.DockWidgetVerticalTitleBar` is set on :sip:ref:`~PyQt6.QtWidgets.QDockWidget`, the title bar widget is repositioned accordingly. In resizeEvent(), the title bar should check what orientation it should assume:

  .. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdockwidget.py
      :lines: 54-59

* The title bar widget must have a valid :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` and :sip:ref:`~PyQt6.QtWidgets.QWidget.minimumSizeHint`. These functions should take into account the current orientation of the title bar.

* It is not possible to remove a title bar from a dock widget. However, a similar effect can be achieved by setting a default constructed `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ as the title bar widget.

Using qobject_cast() as shown above, the title bar widget has full access to its parent :sip:ref:`~PyQt6.QtWidgets.QDockWidget`. Hence it can perform such operations as docking and hiding in response to user actions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDockWidget.titleBarWidget`, :sip:ref:`~PyQt6.QtWidgets.QDockWidget.DockWidgetFeatures.DockWidgetVerticalTitleBar`.
