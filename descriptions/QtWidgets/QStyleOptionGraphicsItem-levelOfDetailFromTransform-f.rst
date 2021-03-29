.. sip:method-description::
    :status: todo
    :pysig: 5ef35d5b554ab2ce8eb6210787f74b6a
    :realsig: (const QTransform&)
    :digest: 9ff049b887e3ca1f985e8be948629432

Returns the level of detail from the *worldTransform*.

Its value represents the maximum value of the height and width of a unity rectangle, mapped using the *worldTransform* of the painter used to draw the item. By default, if no transformations are applied, its value is 1. If zoomed out 1:2, the level of detail will be 0.5, and if zoomed in 2:1, its value is 2.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.minimumRenderSize`.
