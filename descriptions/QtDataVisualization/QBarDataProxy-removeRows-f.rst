.. sip:method-description::
    :status: todo
    :pysig: f6500f88779f7b60fb1bf0077334c77d
    :realsig: (int,int,bool)
    :digest: 02d7bddfd0343d5381ff1971ce5572fb

Removes the number of rows specified by *removeCount* starting at the position *rowIndex*. Attempting to remove rows past the end of the array does nothing. If *removeLabels* is ``true``, the corresponding row labels are also removed. Otherwise, the row labels are not affected.

**Note:** If *removeLabels* is ``false``, the row labels array will be out of sync with the row array if there are labeled rows beyond the removed rows.
