.. sip:class-description::
    :status: todo
    :brief:  TODO
    :digest: 7e83faa0933a36b0862afda27a551fcf

Defines a room for the spatial audio engine.

If the listener is inside a room, first order sound reflections and reverb matching the rooms properties will get applied to the sound field.

A room is always square and defined by its center position, its orientation and dimensions. Each of the 6 walls of the room can be made of different materials that will contribute to the computed reflections and reverb that the listener will experience while being inside the room.

If multiple rooms cover the same position, the engine will use the room with the smallest volume.
