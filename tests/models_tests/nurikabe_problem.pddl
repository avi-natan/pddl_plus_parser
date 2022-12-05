(define (problem random-6x6-35)
(:domain paint-nurikabe)
(:objects
  pos-0-0 pos-0-1 pos-0-2 pos-0-3 pos-0-4 pos-0-5 pos-1-0 pos-1-1 pos-1-2 pos-1-3 pos-1-4 pos-1-5 pos-2-0 pos-2-1 pos-2-2 pos-2-3 pos-2-4 pos-2-5 pos-3-0 pos-3-1 pos-3-2 pos-3-3 pos-3-4 pos-3-5 pos-4-0 pos-4-1 pos-4-2 pos-4-3 pos-4-4 pos-4-5 pos-5-0 pos-5-1 pos-5-2 pos-5-3 pos-5-4 pos-5-5 - cell
  n1 n2 n3 - num
  g0 g1 g2 g3 g4 g5 - group
)
(:init
 (NEXT n0 n1)
 (NEXT n1 n2)
 (NEXT n2 n3)

 (CONNECTED pos-0-0 pos-1-0)
 (CONNECTED pos-0-0 pos-0-1)
 (CONNECTED pos-0-1 pos-1-1)
 (CONNECTED pos-0-1 pos-0-2)
 (CONNECTED pos-0-1 pos-0-0)
 (CONNECTED pos-0-2 pos-1-2)
 (CONNECTED pos-0-2 pos-0-3)
 (CONNECTED pos-0-2 pos-0-1)
 (CONNECTED pos-0-3 pos-1-3)
 (CONNECTED pos-0-3 pos-0-4)
 (CONNECTED pos-0-3 pos-0-2)
 (CONNECTED pos-0-4 pos-1-4)
 (CONNECTED pos-0-4 pos-0-5)
 (CONNECTED pos-0-4 pos-0-3)
 (CONNECTED pos-0-5 pos-1-5)
 (CONNECTED pos-0-5 pos-0-4)
 (CONNECTED pos-1-0 pos-2-0)
 (CONNECTED pos-1-0 pos-1-1)
 (CONNECTED pos-1-0 pos-0-0)
 (CONNECTED pos-1-1 pos-2-1)
 (CONNECTED pos-1-1 pos-1-2)
 (CONNECTED pos-1-1 pos-0-1)
 (CONNECTED pos-1-1 pos-1-0)
 (CONNECTED pos-1-2 pos-2-2)
 (CONNECTED pos-1-2 pos-1-3)
 (CONNECTED pos-1-2 pos-0-2)
 (CONNECTED pos-1-2 pos-1-1)
 (CONNECTED pos-1-3 pos-2-3)
 (CONNECTED pos-1-3 pos-1-4)
 (CONNECTED pos-1-3 pos-0-3)
 (CONNECTED pos-1-3 pos-1-2)
 (CONNECTED pos-1-4 pos-2-4)
 (CONNECTED pos-1-4 pos-1-5)
 (CONNECTED pos-1-4 pos-0-4)
 (CONNECTED pos-1-4 pos-1-3)
 (CONNECTED pos-1-5 pos-2-5)
 (CONNECTED pos-1-5 pos-0-5)
 (CONNECTED pos-1-5 pos-1-4)
 (CONNECTED pos-2-0 pos-3-0)
 (CONNECTED pos-2-0 pos-2-1)
 (CONNECTED pos-2-0 pos-1-0)
 (CONNECTED pos-2-1 pos-3-1)
 (CONNECTED pos-2-1 pos-2-2)
 (CONNECTED pos-2-1 pos-1-1)
 (CONNECTED pos-2-1 pos-2-0)
 (CONNECTED pos-2-2 pos-3-2)
 (CONNECTED pos-2-2 pos-2-3)
 (CONNECTED pos-2-2 pos-1-2)
 (CONNECTED pos-2-2 pos-2-1)
 (CONNECTED pos-2-3 pos-3-3)
 (CONNECTED pos-2-3 pos-2-4)
 (CONNECTED pos-2-3 pos-1-3)
 (CONNECTED pos-2-3 pos-2-2)
 (CONNECTED pos-2-4 pos-3-4)
 (CONNECTED pos-2-4 pos-2-5)
 (CONNECTED pos-2-4 pos-1-4)
 (CONNECTED pos-2-4 pos-2-3)
 (CONNECTED pos-2-5 pos-3-5)
 (CONNECTED pos-2-5 pos-1-5)
 (CONNECTED pos-2-5 pos-2-4)
 (CONNECTED pos-3-0 pos-4-0)
 (CONNECTED pos-3-0 pos-3-1)
 (CONNECTED pos-3-0 pos-2-0)
 (CONNECTED pos-3-1 pos-4-1)
 (CONNECTED pos-3-1 pos-3-2)
 (CONNECTED pos-3-1 pos-2-1)
 (CONNECTED pos-3-1 pos-3-0)
 (CONNECTED pos-3-2 pos-4-2)
 (CONNECTED pos-3-2 pos-3-3)
 (CONNECTED pos-3-2 pos-2-2)
 (CONNECTED pos-3-2 pos-3-1)
 (CONNECTED pos-3-3 pos-4-3)
 (CONNECTED pos-3-3 pos-3-4)
 (CONNECTED pos-3-3 pos-2-3)
 (CONNECTED pos-3-3 pos-3-2)
 (CONNECTED pos-3-4 pos-4-4)
 (CONNECTED pos-3-4 pos-3-5)
 (CONNECTED pos-3-4 pos-2-4)
 (CONNECTED pos-3-4 pos-3-3)
 (CONNECTED pos-3-5 pos-4-5)
 (CONNECTED pos-3-5 pos-2-5)
 (CONNECTED pos-3-5 pos-3-4)
 (CONNECTED pos-4-0 pos-5-0)
 (CONNECTED pos-4-0 pos-4-1)
 (CONNECTED pos-4-0 pos-3-0)
 (CONNECTED pos-4-1 pos-5-1)
 (CONNECTED pos-4-1 pos-4-2)
 (CONNECTED pos-4-1 pos-3-1)
 (CONNECTED pos-4-1 pos-4-0)
 (CONNECTED pos-4-2 pos-5-2)
 (CONNECTED pos-4-2 pos-4-3)
 (CONNECTED pos-4-2 pos-3-2)
 (CONNECTED pos-4-2 pos-4-1)
 (CONNECTED pos-4-3 pos-5-3)
 (CONNECTED pos-4-3 pos-4-4)
 (CONNECTED pos-4-3 pos-3-3)
 (CONNECTED pos-4-3 pos-4-2)
 (CONNECTED pos-4-4 pos-5-4)
 (CONNECTED pos-4-4 pos-4-5)
 (CONNECTED pos-4-4 pos-3-4)
 (CONNECTED pos-4-4 pos-4-3)
 (CONNECTED pos-4-5 pos-5-5)
 (CONNECTED pos-4-5 pos-3-5)
 (CONNECTED pos-4-5 pos-4-4)
 (CONNECTED pos-5-0 pos-5-1)
 (CONNECTED pos-5-0 pos-4-0)
 (CONNECTED pos-5-1 pos-5-2)
 (CONNECTED pos-5-1 pos-4-1)
 (CONNECTED pos-5-1 pos-5-0)
 (CONNECTED pos-5-2 pos-5-3)
 (CONNECTED pos-5-2 pos-4-2)
 (CONNECTED pos-5-2 pos-5-1)
 (CONNECTED pos-5-3 pos-5-4)
 (CONNECTED pos-5-3 pos-4-3)
 (CONNECTED pos-5-3 pos-5-2)
 (CONNECTED pos-5-4 pos-5-5)
 (CONNECTED pos-5-4 pos-4-4)
 (CONNECTED pos-5-4 pos-5-3)
 (CONNECTED pos-5-5 pos-4-5)
 (CONNECTED pos-5-5 pos-5-4)

 (robot-pos pos-0-0)
 (moving)

 (SOURCE pos-0-0 g0)
 (SOURCE pos-2-0 g1)
 (SOURCE pos-4-1 g2)
 (SOURCE pos-0-2 g3)
 (SOURCE pos-3-3 g4)
 (SOURCE pos-1-5 g5)

 (available pos-0-4)
 (available pos-1-1)
 (available pos-1-3)
 (available pos-2-2)
 (available pos-2-4)
 (available pos-3-5)
 (available pos-4-4)
 (available pos-4-5)
 (available pos-5-0)
 (available pos-5-2)
 (available pos-5-3)
 (available pos-5-4)
 (available pos-5-5)
 (blocked pos-1-0)
 (blocked pos-0-1)
 (part-of pos-3-0 g1)
 (part-of pos-2-1 g1)
 (part-of pos-5-1 g2)
 (part-of pos-4-2 g2)
 (part-of pos-3-1 g2)
 (part-of pos-4-0 g2)
 (part-of pos-1-2 g3)
 (part-of pos-0-3 g3)
 (part-of pos-4-3 g4)
 (part-of pos-3-4 g4)
 (part-of pos-2-3 g4)
 (part-of pos-3-2 g4)
 (part-of pos-2-5 g5)
 (part-of pos-0-5 g5)
 (part-of pos-1-4 g5)
 (remaining-cells g0 n1)
 (remaining-cells g1 n2)
 (remaining-cells g2 n3)
 (remaining-cells g3 n3)
 (remaining-cells g4 n3)
 (remaining-cells g5 n1)
)
(:goal (and
 (group-painted g0)
 (group-painted g1)
 (group-painted g2)
 (group-painted g3)
 (group-painted g4)
 (group-painted g5)
))
)

