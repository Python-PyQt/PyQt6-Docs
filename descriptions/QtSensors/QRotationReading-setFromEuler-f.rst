.. sip:method-description::
    :status: todo
    :pysig: eed5c663a9110c04fdce085b268c2b9d
    :realsig: (qreal,qreal,qreal)
    :digest: 529bbd9ed5d081b9bf9850c7f50ffdf0

Sets the rotation from three euler angles.

This is to be called from the backend.

The angles are measured in degrees. The order of the rotations matters, as first the *z* rotation is applied, then the *x* rotation and finally the *y* rotation.
