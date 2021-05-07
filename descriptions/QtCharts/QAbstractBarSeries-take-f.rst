.. sip:method-description::
    :status: todo
    :pysig: 201bb307b6ac3a682b13dad52e1b4798
    :realsig: (QBarSet*)
    :digest: 2cb2bda82094fc7ead01443a2f277201

Takes a single *set* from the series. Does not delete the bar set object.

**Note:** The series remains the barset's parent object. You must set the parent object to take full ownership.

Returns ``true`` if the take operation succeeds.
