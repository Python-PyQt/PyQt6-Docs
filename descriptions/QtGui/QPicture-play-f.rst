.. sip:method-description::
    :status: todo
    :pysig: 484c3f34a341b4fe2b28b029a84f4c9a
    :realsig: (QPainter*)
    :digest: 8b96cfaddb1398e672f373f5051d844f

Replays the picture using *painter*, and returns ``true`` if successful; otherwise returns ``false``.

This function does exactly the same as :sip:ref:`~PyQt6.QtGui.QPainter.drawPicture` with (x, y) = (0, 0).

**Note:** The state of the painter isn't preserved by this function.
