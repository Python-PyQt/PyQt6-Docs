.. sip:class-description::
    :status: todo
    :brief: Specifies the size of rasterized points. May either be set statically or by shader programs
    :realname: Qt3DRender::QPointSize
    :digest: a08773d39898a7ed018e0ef7075ae847

Specifies the size of rasterized points. May either be set statically or by shader programs.

When the :sip:ref:`~PyQt6.Qt3DRender.QPointSize.sizeMode` property is set to SizeMode::Fixed, the value is set using glPointSize(), if available. When using SizeMode::Programmable, gl_PointSize must be set within shader programs, the value provided to this `RenderState <https://doc.qt.io/qt-6/qml-qt3d-render-renderstate.html>`_ is ignored in that case.
