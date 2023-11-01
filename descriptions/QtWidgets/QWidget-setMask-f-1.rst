.. sip:method-description::
    :status: todo
    :pysig: 7b302619a1f8d21d9efa913403e8d56b
    :realsig: (const QRegion&)
    :digest: 53d9dd0d257c73781f41710b45fd99aa

This is an overloaded function.

Causes only the parts of the widget which overlap *region* to be visible. If the region includes pixels outside the :sip:ref:`~PyQt6.QtWidgets.QWidget.rect` of the widget, window system controls in that area may or may not be visible, depending on the platform.

Since :sip:ref:`~PyQt6.QtGui.QRegion` allows arbitrarily complex regions to be created, widget masks can be made to suit the most unconventionally-shaped windows, and even allow widgets to be displayed with holes in them. Note that this effect can be slow if the region is particularly complex.

Widget masks are used to hint to the window system that the application does not want mouse events for areas outside the mask. On most systems, they also result in coarse visual clipping. To get smooth window edges, use translucent background and anti-aliased painting instead, as shown in the `Translucent Background <https://doc.qt.io/qt-6/qtwidgets-widgets-shapedclock-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.windowOpacity`.
