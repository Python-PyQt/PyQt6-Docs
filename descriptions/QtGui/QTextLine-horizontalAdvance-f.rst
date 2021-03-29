.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 18312e8ec580f9ba244557d7695a8f8e

Returns the horizontal advance of the text. The advance of the text is the distance from its position to the next position at which text would naturally be drawn.

By adding the advance to the position of the text line and using this as the position of a second text line, you will be able to position the two lines side-by-side without gaps in-between.
