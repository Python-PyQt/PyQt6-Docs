.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: ()
    :digest: 2d1ebf3ec8fc25736a63f796d393f734

Reads and returns the raw inner XML content of the current element. This function is useful for retrieving the full contents embedded inside an element, including nested tags, text, comments, processing instructions, CDATA sections, and other markup — preserving the original XML structure.

The current element is the element matching the most recently parsed start element of which a matching end element has not yet been reached. When the parser has reached the end element, the current element becomes the parent element.

**Note:** Entity references defined in the DTD are resolved during parsing and returned as plain text, since DTD declarations are processed separately and are not part of the element’s content. Only the five predefined XML entities (``&lt;``, ``&gt;``, ``&amp;``, ``&apos;``, ``&quot``;) are re-escaped in the output.
