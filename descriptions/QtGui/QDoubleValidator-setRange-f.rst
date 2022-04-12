.. sip:method-description::
    :status: todo
    :pysig: bccf279b6f2cf3c9034c94231ece625d
    :realsig: (double,double,int)
    :digest: 8243362cdb830845bde3a1cf6ab77e90

Sets the validator to accept doubles from *minimum* to *maximum* inclusive, with at most *decimals* digits after the decimal point.

**Note:** Setting the number of decimals to -1 effectively sets it to unlimited. This is also the value used by a default-constructed validator.
