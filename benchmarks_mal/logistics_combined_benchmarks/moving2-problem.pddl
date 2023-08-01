(define (problem moving1)
    (:domain moving)
    (:objects
        loc00 - location
        loc01 - location
        loc02 - location
        loc10 - location
        loc11 - location
        loc12 - location
        loc20 - location
        loc21 - location
        loc22 - location
        east - direction
        west - direction
        south - direction
        north - direction
        tru1 - truck
        tru2 - truck
        tru3 - truck
    )
    (:init
        (dirof loc01 east loc00)
        (dirof loc02 east loc01)
        (dirof loc11 east loc10)
        (dirof loc12 east loc11)
        (dirof loc21 east loc20)
        (dirof loc22 east loc21)
        (dirof loc10 south loc00)
        (dirof loc20 south loc10)
        (dirof loc11 south loc01)
        (dirof loc21 south loc11)
        (dirof loc12 south loc02)
        (dirof loc22 south loc12)
        (dirof loc01 west loc02)
        (dirof loc00 west loc01)
        (dirof loc11 west loc12)
        (dirof loc10 west loc11)
        (dirof loc21 west loc22)
        (dirof loc20 west loc21)
        (dirof loc10 north loc20)
        (dirof loc00 north loc10)
        (dirof loc11 north loc21)
        (dirof loc01 north loc11)
        (dirof loc12 north loc22)
        (dirof loc02 north loc12)
        (rightof east north)
        (rightof south east)
        (rightof west south)
        (rightof north west)
        (leftof east south)
        (leftof north east)
        (leftof west north)
        (leftof south west)
        (at tru1 loc00)
        (at tru2 loc01)
        (at tru3 loc02)
        (empty loc10)
        (empty loc11)
        (empty loc12)
        (empty loc20)
        (empty loc21)
        (empty loc22)
        (facedir tru1 east)
        (facedir tru2 north)
        (facedir tru3 east)
    )
    (:goal
        (and
            (at tru1 loc11)
            (at tru2 loc21)
            (at tru3 loc20)
        )
    )
)