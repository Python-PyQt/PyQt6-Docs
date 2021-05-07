.. sip:method-description::
    :status: todo
    :pysig: 7391025762bc8f48f5353c7e0b1b6e0b
    :realsig: (QBoxSet*)
    :digest: 2bebba51abbdfb2a12b1db8940e64433

Takes the box-and-whiskers item specified by *set* from the series. Does not delete the item.

**Note:** The series remains the item's parent object. You must set the parent object to take full ownership.

Returns ``true`` if the take operation succeeds.
