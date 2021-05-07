.. sip:method-description::
    :status: todo
    :pysig: ea745d62d241f21af585c6b5e658fbeb
    :realsig: (int,const QBarDataArray&)
    :digest: 7ac3b7753a8ab0053b05ec9d4903b1ea

Inserts new *rows* into *rowIndex*. If *rowIndex* is equal to the array size, the rows are added to the end of the array. The existing row labels are not affected.

**Note:** The row labels array will be out of sync with the row array after this call if there were labeled rows beyond the inserted rows.
