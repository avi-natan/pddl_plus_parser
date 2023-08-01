(define (domain moving)
    (:requirements :typing)
    (:types 
        location truck - object
    )
    (:predicates
        (eastof ?obj1 - object ?obj2 - object)
        (westof ?obj1 - object ?obj2 - object)
        (southof ?obj1 - object ?obj2 - object)
        (northof ?obj1 - object ?obj2 - object)
        (faceeast ?t - truck)
        (facewest ?t - truck)
        (facesouth ?t - truck)
        (facenorth ?t - truck)
        (at ?t - truck ?loc - location)
        (empty ?loc - location)
    )
    (:action move-east
        :parameters     (?t - truck ?lf - location ?lt - location)
        :precondition   (and (at ?t ?lf) (faceeast ?t) (eastof ?lt ?lf) (empty ?lt))
        :effect         (and (not (at ?t ?lf)) (empty ?lf) (faceeast ?t) (not (empty ?lt)) (at ?t ?lt))
    )
    (:action move-west
        :parameters     (?t - truck ?lf - location ?lt - location)
        :precondition   (and (at ?t ?lf) (facewest ?t) (westof ?lt ?lf) (empty ?lt))
        :effect         (and (not (at ?t ?lf)) (empty ?lf) (facewest ?t) (not (empty ?lt)) (at ?t ?lt))
    )
    (:action move-south
        :parameters     (?t - truck ?lf - location ?lt - location)
        :precondition   (and (at ?t ?lf) (facesouth ?t) (southof ?lt ?lf) (empty ?lt))
        :effect         (and (not (at ?t ?lf)) (empty ?lf) (facesouth ?t) (not (empty ?lt)) (at ?t ?lt))
    )
    (:action move-north
        :parameters     (?t - truck ?lf - location ?lt - location)
        :precondition   (and (at ?t ?lf) (facenorth ?t) (northof ?lt ?lf) (empty ?lt))
        :effect         (and (not (at ?t ?lf)) (empty ?lf) (facenorth ?t) (not (empty ?lt)) (at ?t ?lt))
    )
    (:action rotate-east-south
        :parameters     (?t - truck)
        :precondition   (and (faceeast ?t))
        :effect         (and (facesouth ?t) (not (faceeast ?t)))
    )
    (:action rotate-south-west
        :parameters     (?t - truck)
        :precondition   (and (facesouth ?t))
        :effect         (and (facewest ?t) (not (facesouth ?t)))
    )
    (:action rotate-west-north
        :parameters     (?t - truck)
        :precondition   (and (facewest ?t))
        :effect         (and (facenorth ?t) (not (facewest ?t)))
    )
    (:action rotate-north-east
        :parameters     (?t - truck)
        :precondition   (and (facenorth ?t))
        :effect         (and (faceeast ?t) (not (facenorth ?t)))
    )
    (:action rotate-east-north
        :parameters     (?t - truck)
        :precondition   (and (faceeast ?t))
        :effect         (and (facenorth ?t) (not (faceeast ?t)))
    )
    (:action rotate-north-west
        :parameters     (?t - truck)
        :precondition   (and (facenorth ?t))
        :effect         (and (facewest ?t) (not (facenorth ?t)))
    )
    (:action rotate-west-south
        :parameters     (?t - truck)
        :precondition   (and (facewest ?t))
        :effect         (and (facesouth ?t) (not (facewest ?t)))
    )
    (:action rotate-south-east
        :parameters     (?t - truck)
        :precondition   (and (facesouth ?t))
        :effect         (and (faceeast ?t) (not (facesouth ?t)))
    )
    
)