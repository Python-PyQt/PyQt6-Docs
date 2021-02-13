.. sip:method-description::
    :status: todo
    :pysig: 569e090b4a251ef5c585ecec17d3de3e
    :realsig: (QGraphicsWidget*,QGraphicsWidget*)
    :digest: d29de413efb0c3f7deaea04bb22e46ce

Moves the *second* widget around the ring of focus widgets so that keyboard focus moves from the *first* widget to the *second* widget when the Tab key is pressed.

Note that since the tab order of the *second* widget is changed, you should order a chain like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicswidget.py
    :lines: 67-69

*not* like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicswidget.py
    :lines: 74-77

If *first* is ``nullptr``, this indicates that *second* should be the first widget to receive input focus should the scene gain Tab focus (i.e., the user hits Tab so that focus passes into the scene). If *second* is ``nullptr``, this indicates that *first* should be the first widget to gain focus if the scene gained BackTab focus.

By default, tab order is defined implicitly using widget creation order.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.focusPolicy`, `Keyboard Focus in Widgets <https://doc.qt.io/qt-6/focus.html>`_.
