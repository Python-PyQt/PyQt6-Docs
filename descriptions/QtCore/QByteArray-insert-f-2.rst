.. sip:method-description::
    :status: todo
    :pysig: 84050eacd8a006c3ee0ffec7956f9ff7
    :realsig: (qsizetype,qsizetype,char)
    :digest: 80844b8e54ac8bece29e5715b9ddd4e1

Inserts *count* copies of byte *ch* at index position *i* in the byte array.

This array grows to accommodate the insertion. If *i* is beyond the end of the array, the array is first extended with space characters to reach this *i*.
