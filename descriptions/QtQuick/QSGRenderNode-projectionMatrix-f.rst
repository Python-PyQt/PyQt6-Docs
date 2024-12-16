.. sip:method-description::
    :status: todo
    :pysig: f7702f3ac6e67cbda38e195e36b612a6
    :realsig: () const
    :digest: 839148cc843ad8f7bbd21c5169c916f2

Returns pointer to the current projection matrix.

In :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` this is the same matrix that is returned from RenderState::projectionMatrix(). This getter exists so that :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.prepare` also has a way to query the projection matrix.

When working with a modern graphics API, or Qt's own graphics abstraction layer, it is more than likely that one will want to load ``\*projectionMatrix() \* \*matrix()`` into a uniform buffer. That is however something that needs to be done in :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.prepare`, so outside the recording of a render pass. That is why both matrices are queriable directly from the :sip:ref:`~PyQt6.QtQuick.QSGRenderNode`, both in :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.prepare` and :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.
