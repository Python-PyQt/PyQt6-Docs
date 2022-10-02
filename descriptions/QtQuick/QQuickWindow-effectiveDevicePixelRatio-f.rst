.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: b183661205964f2d1370fc495fc1aeb5

Returns the device pixel ratio for this window.

This is different from :sip:ref:`~PyQt6.QtGui.QWindow.devicePixelRatio` in that it supports redirected rendering via :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` and :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`. When using a :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is often not fully created, meaning it is never shown and there is no underlying native window created in the windowing system. As a result, querying properties like the device pixel ratio cannot give correct results. This function takes into account both :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.renderWindowFor` and :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget.devicePixelRatio`. When no redirection is in effect, the result is same as :sip:ref:`~PyQt6.QtGui.QWindow.devicePixelRatio`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtGui.QWindow.devicePixelRatio`.
