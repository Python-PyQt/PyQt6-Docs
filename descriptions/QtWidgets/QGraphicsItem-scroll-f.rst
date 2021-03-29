.. sip:method-description::
    :status: todo
    :pysig: 3f8044940c07cce4209327671783e122
    :realsig: (qreal,qreal,const QRectF&)
    :digest: ec31d621e714e1f8c1b40051d6626a4a

Scrolls the contents of *rect* by *dx*, *dy*. If *rect* is a null rect (the default), the item's bounding rect is scrolled.

Scrolling provides a fast alternative to simply redrawing when the contents of the item (or parts of the item) are shifted vertically or horizontally. Depending on the current transformation and the capabilities of the paint device (i.e., the viewport), this operation may consist of simply moving pixels from one location to another using memmove(). In most cases this is faster than rerendering the entire area.

After scrolling, the item will issue an update for the newly exposed areas. If scrolling is not supported (e.g., you are rendering to an OpenGL viewport, which does not benefit from scroll optimizations), this function is equivalent to calling update(\ *rect*).

**Note:** Scrolling is only supported when :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.ItemCoordinateCache` is enabled; in all other cases calling this function is equivalent to calling update(\ *rect*). If you for sure know that the item is opaque and not overlapped by other items, you can map the *rect* to viewport coordinates and scroll the viewport.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 271-273

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`.
