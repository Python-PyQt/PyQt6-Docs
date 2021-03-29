.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: () const
    :digest: 756439529fb7a08c7fc38ead147b5283

Returns the current mouse grabber item, or ``nullptr`` if no item is currently grabbing the mouse. The mouse grabber item is the item that receives all mouse events sent to the scene.

An item becomes a mouse grabber when it receives and accepts a mouse press event, and it stays the mouse grabber until either of the following events occur:

* If the item receives a mouse release event when there are no other buttons pressed, it loses the mouse grab.

* If the item becomes invisible (i.e., someone calls ``item->setVisible(false)``), or if it becomes disabled (i.e., someone calls ``item->setEnabled(false)``), it loses the mouse grab.

* If the item is removed from the scene, it loses the mouse grab.

If the item loses its mouse grab, the scene will ignore all mouse events until a new item grabs the mouse (i.e., until a new item receives a mouse press event).
