.. sip:method-description::
    :status: todo
    :pysig: d917a5c509e30cbf87a77f29e5d8f2c9
    :realsig: (int,QBarDataRow*)
    :digest: d0adb4067af2a1bca2f9fe5f3ae51b04

Inserts the new row *row* into *rowIndex*. If *rowIndex* is equal to the array size, the rows are added to the end of the array. The existing row labels are not affected.

**Note:** The row labels array will be out of sync with the row array after this call if there were labeled rows beyond the inserted row.
