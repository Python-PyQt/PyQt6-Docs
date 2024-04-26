.. sip:method-description::
    :status: todo
    :pysig: 01479a9ddeacdcf684a3b7e6e4ffb09a
    :realsig: (int,const QPointF&,qreal)
    :digest: 7447ec8ef28b743ada4cc973bf4efc34

Adds the given destination, consisting of *page*, *location*, and *zoom*, to the history of visited locations.

The *zoom* argument represents magnification (where ``1`` is the default scale, 1 logical pixel = 1 point). If *zoom* is not given or is ``0``, :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.currentZoom` keeps its existing value, and :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.currentZoomChanged` is not emitted.

The *location* should be the same as :sip:ref:`~PyQt6.QtPdf.QPdfLink.location` if the user is following a link; and since that is specified as the upper-left corner of the destination, it is best for consistency to always use the location visible in the upper-left corner of the viewport, in points.

If :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.forwardAvailable` is ``true``, calling this function represents a branch in the timeline which causes the "future" to be lost, and therefore :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.forwardAvailable` will change to ``false``.
