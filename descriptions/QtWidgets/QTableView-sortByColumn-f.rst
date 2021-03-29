.. sip:method-description::
    :status: todo
    :pysig: eba4956196cd20b697eab7612d06a13b
    :realsig: (int,Qt::SortOrder)
    :digest: 23521014a5ae62951b69e549557db307

Sorts the model by the values in the given *column* and *order*.

*column* may be -1, in which case no sort indicator will be shown and the model will return to its natural, unsorted order. Note that not all models support this and may even crash in this case.

.. seealso:: sortingEnabled.
