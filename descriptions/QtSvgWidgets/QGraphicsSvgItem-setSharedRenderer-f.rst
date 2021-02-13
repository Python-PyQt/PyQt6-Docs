.. sip:method-description::
    :status: todo
    :pysig: aa8b28e0ba0cf721bad2211ae2e8437b
    :realsig: (QSvgRenderer*)
    :digest: 4864eaa32590272dc5d172dcfc22af17

Sets *renderer* to be a shared :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` on the item. By using this method one can share the same :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` on a number of items. This means that the SVG file will be parsed only once. :sip:ref:`~PyQt6.QtSvg.QSvgRenderer` passed to this method has to exist for as long as this item is used.
