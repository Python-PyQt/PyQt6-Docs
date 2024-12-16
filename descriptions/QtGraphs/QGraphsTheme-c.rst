.. sip:class-description::
    :status: todo
    :brief: Visual style for graphs
    :digest: 42dcb2f801b120430b8f5bfe9335aed9

:sip:ref:`~PyQt6.QtGraphs.QGraphsTheme` class provides a visual style for graphs.

Specifies visual properties that affect the whole graph. There are several built-in themes that can be used as is or modified freely.

Themes can be created from scratch using the :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.Theme.UserDefined` enum value. Creating a theme using the default constructor produces a new user-defined theme.

.. _qgraphstheme-customizing-theme:

Customizing Theme
-----------------

The default theme is :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.Theme.QtGreen`, but it is possible to customize each property.

The following table lists the properties controlled by a theme and the default values for :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.Theme.UserDefined`.

+---------------------------------------------------------+-------------------------------------------------------------------+
| Property                                                | Default Value                                                     |
+=========================================================+===================================================================+
| backgroundVisible                                       | ``true``                                                          |
+---------------------------------------------------------+-------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.seriesColors`    | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.black`                     |
+---------------------------------------------------------+-------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.seriesGradients` | :sip:ref:`~PyQt6.QtGui.QLinearGradient`. Essentially fully black. |
+---------------------------------------------------------+-------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.colorStyle`      | Uniform                                                           |
+---------------------------------------------------------+-------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.labelFont`       | :sip:ref:`~PyQt6.QtGui.QFont`                                     |
+---------------------------------------------------------+-------------------------------------------------------------------+
| gridVisible                                             | ``true``                                                          |
+---------------------------------------------------------+-------------------------------------------------------------------+
| labelBackgroundVisible                                  | ``true``                                                          |
+---------------------------------------------------------+-------------------------------------------------------------------+
| labelBorderVisible                                      | ``true``                                                          |
+---------------------------------------------------------+-------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGraphs.QGraphsTheme.labelsVisible`   | ``true``                                                          |
+---------------------------------------------------------+-------------------------------------------------------------------+

.. _qgraphstheme-usage-examples:

Usage Examples
--------------

Creating a built-in theme without any modifications:

.. literalinclude:: ../../../snippets/qtgraphs-src-doc-snippets-doc_src_qgraphstheme.py
    :lines: 16-16

Creating a built-in theme and modifying some properties:

.. literalinclude:: ../../../snippets/qtgraphs-src-doc-snippets-doc_src_qgraphstheme.py
    :lines: 15-19

Modifying a user-defined theme. The theme has been created the same way it was in the previous snippets:

.. literalinclude:: ../../../snippets/qtgraphs-src-doc-snippets-doc_src_qgraphstheme.py
    :lines: 23-40

Modifying some properties after theme has been set to a graph:

.. literalinclude:: ../../../snippets/qtgraphs-src-doc-snippets-doc_src_qgraphstheme.py
    :lines: 44-51
