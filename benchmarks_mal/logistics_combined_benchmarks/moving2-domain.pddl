(define (domain moving)
    (:requirements :typing)
    (:types 
        location truck direction - object
    )
    (:predicates
        (dirof ?obj1 - object ?dir - direction ?obj2 - object)
        (rightof ?dir1 - direction ?dir2 - direction)
        (leftof ?dir1 - direction ?dir2 - direction)
        (facedir ?t - truck ?dir - direction)
        (at ?t - truck ?loc - location)
        (empty ?loc - location)
    )
    (:action move-forward
        :parameters     (?t - truck ?lf - location ?dir - direction ?lt - location)
        :precondition   (and (at ?t ?lf) (facedir ?t ?dir) (dirof ?lt ?dir ?lf) (empty ?lt))
        :effect         (and (not (at ?t ?lf)) (empty ?lf) (facedir ?t ?dir) (not (empty ?lt)) (at ?t ?lt))
    )
    (:action rotate-right
        :parameters     (?t - truck ?df - direction ?dt - direction)
        :precondition   (and (facedir ?t ?df) (rightof ?dt ?df))
        :effect         (and (facedir ?t ?dt) (not (facedir ?t ?df)))
    )
    (:action rotate-left
        :parameters     (?t - truck ?df - direction ?dt - direction)
        :precondition   (and (facedir ?t ?df) (leftof ?dt ?df))
        :effect         (and (facedir ?t ?dt) (not (facedir ?t ?df)))
    )
    
)