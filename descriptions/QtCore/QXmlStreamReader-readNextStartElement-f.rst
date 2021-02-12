.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 961d7426848dcc69d61bdaab75e60f15

Reads until the next start element within the current element. Returns ``true`` when a start element was reached. When the end element was reached, or when an error occurred, false is returned.

The current element is the element matching the most recently parsed start element of which a matching end element has not yet been reached. When the parser has reached the end element, the current element becomes the parent element.

This is a convenience function for when you're only concerned with parsing XML elements. The QXmlStream Bookmarks Example makes extensive use of this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.readNext`.
