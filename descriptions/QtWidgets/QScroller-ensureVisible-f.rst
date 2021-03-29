.. sip:method-description::
    :status: todo
    :pysig: b5f637b83de183876dea2bb16cd46020
    :realsig: (const QRectF&,qreal,qreal)
    :digest: d5f01d1e9507f6d83acfa79453332b57

Starts scrolling so that the rectangle *rect* is visible inside the viewport with additional margins specified in pixels by *xmargin* and *ymargin* around the rect.

In cases where it is not possible to fit the rect plus margins inside the viewport the contents are scrolled so that as much as possible is visible from *rect*.

The scrolling speed is calculated so that the given position is reached after a platform-defined time span.

This function performs the actual scrolling by calling :sip:ref:`~PyQt6.QtWidgets.QScroller.scrollTo`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScroller.scrollTo`.
