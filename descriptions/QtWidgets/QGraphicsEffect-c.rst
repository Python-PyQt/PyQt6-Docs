.. sip:class-description::
    :status: todo
    :brief: The base class for all graphics effects
    :digest: 5dcda8aedf41698a9713d91ceaea71ef

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect` class is the base class for all graphics effects.

Effects alter the appearance of elements by hooking into the rendering pipeline and operating between the source (e.g., a :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`) and the destination device (e.g., :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`'s viewport). Effects can be disabled by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.setEnabled`\ (false). If effects are disabled, the source is rendered directly.

To add a visual effect to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, for example, you can use one of the standard effects, or alternately, create your own effect by creating a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect`. The effect can then be installed on the item using :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setGraphicsEffect`.

Qt provides the following standard effects:

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsBlurEffect` - blurs the item by a given radius

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsDropShadowEffect` - renders a dropshadow behind the item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsColorizeEffect` - renders the item in shades of any given color

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsOpacityEffect` - renders the item with an opacity

+-------------------------------------------------------+-----------------------------------------------------------+
| .. image:: ../../../images/graphicseffect-plain.png   |                                                           |
+-------------------------------------------------------+-----------------------------------------------------------+
| .. image:: ../../../images/graphicseffect-blur.png    | .. image:: ../../../images/graphicseffect-colorize.png    |
+-------------------------------------------------------+-----------------------------------------------------------+
| .. image:: ../../../images/graphicseffect-opacity.png | .. image:: ../../../images/graphicseffect-drop-shadow.png |
+-------------------------------------------------------+-----------------------------------------------------------+

.. image:: ../../../images/graphicseffect-widget.png

For more information on how to use each effect, refer to the specific effect's documentation.

To create your own custom effect, create a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect` (or any other existing effects) and reimplement the virtual function :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw`. This function is called whenever the effect needs to redraw. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw` function takes the painter with which to draw as an argument. For more information, refer to the documenation for :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw`. In the :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw` function you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.sourcePixmap` to get a pixmap of the graphics effect source which you can then process.

If your effect changes, use :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.update` to request for a redraw. If your custom effect changes the bounding rectangle of the source, e.g., a radial glow effect may need to apply an extra margin, you can reimplement the virtual :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.boundingRectFor` function, and call :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.updateBoundingRect` to notify the framework whenever this rectangle changes. The virtual :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.sourceChanged` function is called to notify the effects that the source has changed in some way - e.g., if the source is a :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem` and its rectangle parameters have changed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setGraphicsEffect`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setGraphicsEffect`.
