.. sip:class-description::
    :status: todo
    :brief: Proxy layer for embedding a QWidget in a QGraphicsScene
    :digest: 38f0505795116eb6ee96e34ed67bcc6a

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` class provides a proxy layer for embedding a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ in a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` embeds `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_-based widgets, for example, a :sip:ref:`~PyQt6.QtWidgets.QPushButton`, :sip:ref:`~PyQt6.QtWidgets.QFontComboBox`, or even :sip:ref:`~PyQt6.QtWidgets.QFileDialog`, into :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`. It forwards events between the two objects and translates between `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_'s integer-based geometry and `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_'s qreal-based geometry. :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` supports all core features of `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, including tab focus, keyboard input, Drag & Drop, and popups. You can also embed complex widgets, e.g., widgets with subwidgets.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsproxywidget.py
    :lines: 54-67

:sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` takes care of automatically embedding popup children of embedded widgets through creating a child proxy for each popup. This means that when an embedded `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_ shows its popup list, a new :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` is created automatically, embedding the popup, and positioning it correctly. This only works if the popup is child of the embedded widget (for example :sip:ref:`~PyQt6.QtWidgets.QToolButton.setMenu` requires the :sip:ref:`~PyQt6.QtWidgets.QMenu` instance to be child of the :sip:ref:`~PyQt6.QtWidgets.QToolButton`).

.. _qgraphicsproxywidget-embedding-a-widget-with-qgraphicsproxywidget:

Embedding a Widget with QGraphicsProxyWidget
--------------------------------------------

There are two ways to embed a widget using :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget`. The most common way is to pass a widget pointer to :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget` together with any relevant Qt::WindowFlags. This function returns a pointer to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget`. You can then choose to reparent or position either the proxy, or the embedded widget itself.

For example, in the code snippet below, we embed a group box into the proxy:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsproxywidget.py
    :lines: 71-83

The image below is the output obtained with its contents margin and contents rect labeled.

.. image:: ../../../images/qgraphicsproxywidget-embed.png

Alternatively, you can start by creating a new :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` item, and then call :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.setWidget` to embed a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ later. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.widget` function returns a pointer to the embedded widget. :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` shares ownership with `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, so if either of the two widgets are destroyed, the other widget will be automatically destroyed as well.

.. _qgraphicsproxywidget-synchronizing-widget-states:

Synchronizing Widget States
---------------------------

:sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` keeps its state in sync with the embedded widget. For example, if the proxy is hidden or disabled, the embedded widget will be hidden or disabled as well, and vice versa. When the widget is embedded by calling addWidget(), :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` copies the state from the widget into the proxy, and after that, the two will stay synchronized where possible. By default, when you embed a widget into a proxy, both the widget and the proxy will be visible because a `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ is visible when created (you do not have to call show()). If you explicitly hide the embedded widget, the proxy will also become invisible.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsproxywidget.py
    :lines: 87-98

:sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` maintains symmetry for the following states:

+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ state | :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` state    | Notes                                                                                                                                               |
+============================================================================+===========================================================+=====================================================================================================================================================+
| QWidget::enabled                                                           | QGraphicsProxyWidget::enabled                             |                                                                                                                                                     |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| QWidget::visible                                                           | QGraphicsProxyWidget::visible                             | The explicit state is also symmetric.                                                                                                               |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.geometry`                               | QGraphicsProxyWidget::geometry                            | Geometry is only guaranteed to be symmetric while the embedded widget is visible.                                                                   |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.layoutDirection`                        | QGraphicsProxyWidget::layoutDirection                     |                                                                                                                                                     |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.style`                                  | QGraphicsProxyWidget::style                               |                                                                                                                                                     |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.palette`                                | QGraphicsProxyWidget::palette                             |                                                                                                                                                     |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.font`                                   | QGraphicsProxyWidget::font                                |                                                                                                                                                     |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.cursor`                                 | QGraphicsProxyWidget::cursor                              | The embedded widget overrides the proxy widget cursor. The proxy cursor changes depending on which embedded subwidget is currently under the mouse. |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint`                               | :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.sizeHint` | All size hint functionality from the embedded widget is forwarded by the proxy.                                                                     |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| QWidget::getContentsMargins()                                              | QGraphicsProxyWidget::getContentsMargins()                | Updated once by :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.setWidget`.                                                                         |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWidget.windowTitle`                            | QGraphicsProxyWidget::windowTitle                         | Updated once by :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.setWidget`.                                                                         |
+----------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` keeps the embedded widget in a special state that prevents it from disturbing other widgets (both embedded and not embedded) while the widget is embedded. In this state, the widget may differ slightly in behavior from when it is not embedded.

**Warning:** This class is provided for convenience when bridging QWidgets and QGraphicsItems, it should not be used for high-performance scenarios. In particular, embedding widgets into a scene that is then displayed through a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` that uses an OpenGL viewport will not work for all combinations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`, `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_.
