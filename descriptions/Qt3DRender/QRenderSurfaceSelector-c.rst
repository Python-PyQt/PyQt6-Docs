.. sip:class-description::
    :status: todo
    :brief: Provides a way of specifying the render surface
    :realname: Qt3DRender::QRenderSurfaceSelector
    :digest: 58dbd92eedf3898f45979ae9cd713fee

Provides a way of specifying the render surface.

The :sip:ref:`~PyQt6.Qt3DRender.QRenderSurfaceSelector` can be used to select the surface, where Qt3D renders the content. The surface can either be window surface or offscreen surface. The :sip:ref:`~PyQt6.Qt3DRender.QRenderSurfaceSelector.externalRenderTargetSize` is used to specify the actual size of the surface when offscreen surface is used.

When DPI scaling is used by the system, the logical surface size, which is used by mouse events, and the actual 'physical' size of the surface can differ. The :sip:ref:`~PyQt6.Qt3DRender.QRenderSurfaceSelector.surfacePixelRatio` is the factor to convert the logical size to the physical size.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow`, :sip:ref:`~PyQt6.QtGui.QOffscreenSurface`, :sip:ref:`~PyQt6.QtGui.QSurface`.
