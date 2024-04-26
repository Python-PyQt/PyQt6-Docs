.. sip:method-description::
    :status: todo
    :pysig: d4d85079d3c184e4c59bdc73add11325
    :realsig: (int)
    :digest: 09ea17230363ac5429628e733185252e

Returns the *page* number to be used for display purposes.

For example, a document may have multiple sections with different numbering. Perhaps the preface uses roman numerals, the body starts on page 1, and the appendix starts at A1. Whenever a PDF viewer shows a page number, to avoid confusing the user it should be the same "number" as is printed on the corner of the page, rather than the zero-based page index that we use in APIs (assuming the document author has made the page labels match the printed numbers).

If the document does not have custom page numbering, this function returns ``page + 1``.

.. seealso:: :sip:ref:`~PyQt6.QtPdf.QPdfDocument.pageIndexForLabel`.
