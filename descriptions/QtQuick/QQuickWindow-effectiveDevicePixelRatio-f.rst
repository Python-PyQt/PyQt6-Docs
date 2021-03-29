.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 9e9e43d28ddcdcfcc5671189c4df60a7

Returns the device pixel ratio for this window.

This is different from :sip:ref:`~PyQt6.QtGui.QWindow.devicePixelRatio` in that it supports redirected rendering via :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`. When using a :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is often not created, meaning it is never shown and there is no underlying native window created in the windowing system. As a result, querying properties like the device pixel ratio cannot give correct results. Use this function instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.devicePixelRatio`.
