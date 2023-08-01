(define (domain warehouse)
    (:requirements :typing)
    (:types 
        location truck direction box - object
    )
    (:predicates
        (dirof ?obj1 - object ?dir - direction ?obj2 - object)
        (rightof ?dir1 - direction ?dir2 - direction)
        (leftof ?dir1 - direction ?dir2 - direction)
        (facedir ?t - truck ?dir - direction)
        (at ?obj - object ?loc - location)
        (empty ?loc - location)
        (holding ?t - truck ?b - box)
        (free ?t - truck)
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
    (:action lift-box
        :parameters     (?t - truck ?b - box ?ltru - location ?lbox - location ?trudir - direction)
        :precondition   (and (at ?t ?ltru) (at ?b ?lbox) (dirof ?lbox ?trudir ?ltru) (facedir ?t ?trudir) (free ?t))
        :effect         (and (not (at ?b ?lbox)) (empty ?lbox) (not (free ?t)) (holding ?t ?b))
    )
    (:action drop-box
        :parameters     (?t - truck ?b - box ?ltru - location ?lbox - location ?trudir - direction)
        :precondition   (and (at ?t ?ltru) (empty ?lbox) (dirof ?lbox ?trudir ?ltru) (facedir ?t ?trudir) (holding ?t ?b))
        :effect         (and (not (empty ?lbox)) (at ?b ?lbox) (not (holding ?t ?B)) (free ?t))
    )
    
)