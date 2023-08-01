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
        tru1 - truck
        tru2 - truck
        tru3 - truck
    )
    (:init
        (eastof loc01 loc00)
        (eastof loc02 loc01)
        (eastof loc11 loc10)
        (eastof loc12 loc11)
        (eastof loc21 loc20)
        (eastof loc22 loc21)
        (westof loc01 loc02)
        (westof loc00 loc01)
        (westof loc11 loc12)
        (westof loc10 loc11)
        (westof loc21 loc22)
        (westof loc20 loc21)
        (southof loc10 loc00)
        (southof loc20 loc10)
        (southof loc11 loc01)
        (southof loc21 loc11)
        (southof loc12 loc02)
        (southof loc22 loc12)
        (northof loc10 loc20)
        (northof loc00 loc10)
        (northof loc11 loc21)
        (northof loc01 loc11)
        (northof loc12 loc22)
        (northof loc02 loc12)
        (at tru1 loc00)
        (at tru2 loc01)
        (at tru3 loc02)
        (empty loc10)
        (empty loc11)
        (empty loc12)
        (empty loc20)
        (empty loc21)
        (empty loc22)
        (faceeast tru1)
        (facenorth tru2)
        (faceeast tru3)
    )
    (:goal
        (and
            (at tru1 loc11)
            (at tru2 loc21)
            (at tru3 loc20)
        )
    )
)