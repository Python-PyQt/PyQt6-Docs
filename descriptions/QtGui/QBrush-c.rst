.. sip:class-description::
    :status: todo
    :brief: Defines the fill pattern of shapes drawn by QPainter
    :digest: d04aa60d45465915d4e921c9e1ce9577

The :sip:ref:`~PyQt6.QtGui.QBrush` class defines the fill pattern of shapes drawn by :sip:ref:`~PyQt6.QtGui.QPainter`.

A brush has a style, a color, a gradient and a texture.

The brush :sip:ref:`~PyQt6.QtGui.QBrush.style` defines the fill pattern using the :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle` enum. The default brush style is :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.NoBrush` (depending on how you construct a brush). This style tells the painter to not fill shapes. The standard style for filling is :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.SolidPattern`. The style can be set when the brush is created using the appropriate constructor, and in addition the :sip:ref:`~PyQt6.QtGui.QBrush.setStyle` function provides means for altering the style once the brush is constructed.

.. image:: ../../../images/brush-styles.png

The brush :sip:ref:`~PyQt6.QtGui.QBrush.color` defines the color of the fill pattern. The color can either be one of Qt's predefined colors, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, or any other custom :sip:ref:`~PyQt6.QtGui.QColor`. The currently set color can be retrieved and altered using the :sip:ref:`~PyQt6.QtGui.QBrush.color` and :sip:ref:`~PyQt6.QtGui.QBrush.setColor` functions, respectively.

The :sip:ref:`~PyQt6.QtGui.QBrush.gradient` defines the gradient fill used when the current style is either :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.LinearGradientPattern`, :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.RadialGradientPattern` or :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.ConicalGradientPattern`. Gradient brushes are created by giving a :sip:ref:`~PyQt6.QtGui.QGradient` as a constructor argument when creating the :sip:ref:`~PyQt6.QtGui.QBrush`. Qt provides three different gradients: :sip:ref:`~PyQt6.QtGui.QLinearGradient`, :sip:ref:`~PyQt6.QtGui.QConicalGradient`, and :sip:ref:`~PyQt6.QtGui.QRadialGradient` - all of which inherit :sip:ref:`~PyQt6.QtGui.QGradient`.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-brush-gradientcreationsnippet.py
    :lines: 60-64

The :sip:ref:`~PyQt6.QtGui.QBrush.texture` defines the pixmap used when the current style is :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern`. You can create a brush with a texture by providing the pixmap when the brush is created or by using :sip:ref:`~PyQt6.QtGui.QBrush.setTexture`.

Note that applying :sip:ref:`~PyQt6.QtGui.QBrush.setTexture` makes :sip:ref:`~PyQt6.QtGui.QBrush.style` == :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern`, regardless of previous style settings. Also, calling :sip:ref:`~PyQt6.QtGui.QBrush.setColor` will not make a difference if the style is a gradient. The same is the case if the style is :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern` style unless the current texture is a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_.

The :sip:ref:`~PyQt6.QtGui.QBrush.isOpaque` function returns ``true`` if the brush is fully opaque otherwise false. A brush is considered opaque if:

* The alpha component of the :sip:ref:`~PyQt6.QtGui.QBrush.color` is 255.

* Its :sip:ref:`~PyQt6.QtGui.QBrush.texture` does not have an alpha channel and is not a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_.

* The colors in the :sip:ref:`~PyQt6.QtGui.QBrush.gradient` all have an alpha component that is 255.

+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-brush-outline-png| | To specify the style and color of lines and outlines, use the :sip:ref:`~PyQt6.QtGui.QPainter`'s :sip:ref:`~PyQt6.QtGui.QPen` combined with :sip:ref:`~PyQt6.QtCore.Qt.PenStyle` and :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`: |
|                           |                                                                                                                                                                                                                               |
|                           | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qbrush.py                                                                                                                             |
|                           |     :lines: 63-71                                                                                                                                                                                                             |
|                           |                                                                                                                                                                                                                               |
|                           | Note that, by default, :sip:ref:`~PyQt6.QtGui.QPainter` renders the outline (using the currently set pen) when drawing shapes. Use :sip:ref:`~PyQt6.QtCore.Qt.PenStyle.NoPen` to disable this behavior.                       |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For more information about painting in general, see the `Paint System <https://doc.qt.io/qt-6/paintsystem.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle`, :sip:ref:`~PyQt6.QtGui.QPainter`, :sip:ref:`~PyQt6.QtGui.QColor`.

.. |image-brush-outline-png| image:: ../../../images/brush-outline.png
