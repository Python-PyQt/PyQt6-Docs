.. sip:class-description::
    :status: todo
    :brief: Visual style for graphs
    :digest: 349758ecd28f957f962793460169bec3

:sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme` class provides a visual style for graphs.

Specifies visual properties that affect the whole graph. There are several built-in themes that can be used as is or modified freely.

The following properties can be overridden by using :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DSeries` properties to set them explicitly in the series: :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.baseColors`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.baseGradients`, and :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.colorStyle`.

Themes can be created from scratch using the :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.Theme.ThemeUserDefined` enum value. Creating a theme using the default constructor produces a new user-defined theme.

.. _q3dtheme-default-theme:

Default Theme
-------------

The following table lists the properties controlled by themes and the default values for :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.Theme.ThemeUserDefined`.

+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Property                                                               | Default Value                                                               |
+========================================================================+=============================================================================+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.ambientLightStrength`    | 0.25                                                                        |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.backgroundColor`         | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.black`                               |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| backgroundEnabled                                                      | ``true``                                                                    |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.baseColors`              | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.black`                               |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.baseGradients`           | :sip:ref:`~PyQt6.QtGui.QLinearGradient`. Essentially fully black.           |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.colorStyle`              | :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.ColorStyle.ColorStyleUniform` |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.font`                    | :sip:ref:`~PyQt6.QtGui.QFont`                                               |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| gridEnabled                                                            | ``true``                                                                    |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.gridLineColor`           | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.white`                               |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.highlightLightStrength`  | 7.5                                                                         |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.labelBackgroundColor`    | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.gray`                                |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| labelBackgroundEnabled                                                 | ``true``                                                                    |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| labelBorderEnabled                                                     | ``true``                                                                    |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.labelTextColor`          | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.white`                               |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.lightColor`              | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.white`                               |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.lightStrength`           | 5.0                                                                         |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.multiHighlightColor`     | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.blue`                                |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.multiHighlightGradient`  | :sip:ref:`~PyQt6.QtGui.QLinearGradient`. Essentially fully black.           |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.singleHighlightColor`    | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.red`                                 |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.singleHighlightGradient` | :sip:ref:`~PyQt6.QtGui.QLinearGradient`. Essentially fully black.           |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtDataVisualization.Q3DTheme.windowColor`             | :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.black`                               |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. _q3dtheme-usage-examples:

Usage Examples
--------------

Creating a built-in theme without any modifications:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dtheme.py
    :lines: 38-38

Creating a built-in theme and modifying some properties:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dtheme.py
    :lines: 42-44

Creating a user-defined theme:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dtheme.py
    :lines: 48-66

Creating a built-in theme and modifying some properties after it has been set:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dtheme.py
    :lines: 70-73
