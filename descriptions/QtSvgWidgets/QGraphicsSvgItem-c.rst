.. sip:class-description::
    :status: todo
    :brief: QGraphicsItem that can be used to render the contents of SVG files
    :digest: ecf93710c3ef799581ad094a6ae620c5

The :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem` class is a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` that can be used to render the contents of SVG files.

:sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem` provides a way of rendering SVG files onto :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`. :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem` can be created by passing the SVG file to be rendered to its constructor or by explicit setting a shared :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` on it.

Note that setting :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` on a :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem` doesn't make the item take ownership of the renderer, therefore if using :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem.setSharedRenderer` method one has to make sure that the lifetime of the :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` object will be at least as long as that of the :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem`.

:sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem` provides a way of rendering only parts of the SVG files via the :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem.setElementId`. If :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem.setElementId` method is called, only the SVG element (and its children) with the passed id will be renderer. This provides a convenient way of selectively rendering large SVG files that contain a number of discrete elements. For example the following code renders only jokers from a SVG file containing a whole card deck:

.. literalinclude:: ../../../snippets/qtsvg-src-svg-doc-snippets-src_svg_qgraphicssvgitem.py
    :lines: 54-62

Size of the item can be set via direct manipulation of the items transformation matrix.

By default the SVG rendering is cached using :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.DeviceCoordinateCache` mode to speedup the display of items. Caching can be disabled by passing :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.NoCache` to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setCacheMode` method.

.. seealso:: :sip:ref:`~PyQt6.QtSvgWidgets.QSvgWidget`, :sip:ref:`~PyQt6.Qt SVG C++ Classes`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`.
