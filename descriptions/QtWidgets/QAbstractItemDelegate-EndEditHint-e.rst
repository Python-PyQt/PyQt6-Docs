.. sip:enum-description::
    :status: todo
    :digest: 8923e42f8b86a6125603cacca2d2d1bc

This enum describes the different hints that the delegate can give to the model and view components to make editing data in a model a comfortable experience for the user.

These hints let the delegate influence the behavior of the view:

Note that custom views may interpret the concepts of next and previous differently.

The following hints are most useful when models are used that cache data, such as those that manipulate data locally in order to increase performance or conserve network bandwidth.

Although models and views should respond to these hints in appropriate ways, custom components may ignore any or all of them if they are not relevant.
