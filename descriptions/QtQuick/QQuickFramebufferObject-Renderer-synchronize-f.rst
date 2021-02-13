.. sip:method-description::
    :status: todo
    :pysig: 4c083589f1b3b3fe368866db506bce81
    :realsig: (QQuickFramebufferObject*)
    :digest: 8ee4edc5f670a8d84d118614c36ced11

This function is called as a result of QQuickFramebufferObject::update().

Use this function to update the renderer with changes that have occurred in the item. *item* is the item that instantiated this renderer. The function is called once before the FBO is created.

*For instance, if the item has a color property which is controlled by QML, one should call QQuickFramebufferObject::update() and use  to copy the new color into the renderer so that it can be used to render the next frame.*

This function is the only place when it is safe for the renderer and the item to read and write each others members.
