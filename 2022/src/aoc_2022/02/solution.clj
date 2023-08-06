(ns aoc-2022.02.solution
  (:require [clojure.string :as s]))

(def file (slurp "02/input.txt"))

; Part 1 Rules
; A for Rock, B for Paper, and C for Scissors
; X for Rock, Y for Paper, and Z for Scissors.
; (1 for Rock, 2 for Paper, and 3 for Scissors)
; (0 if you lost, 3 if the round was a draw, and 6 if you won)

(defn part-1 []
  (->> (s/split file #"\n")
       (map #(case %
               "A X" 4
               "A Y" 8
               "A Z" 3
               "B X" 1
               "B Y" 5
               "B Z" 9
               "C X" 7
               "C Y" 2
               "C Z" 6))
       (apply +)))

; Part 2 Rules
; A for Rock, B for Paper, and C for Scissors
; X lose, Y draw, Z win"
; (1 for Rock, 2 for Paper, and 3 for Scissors)
; (0 if you lost, 3 if the round was a draw, and 6 if you won)


(defn part-2 []
  (->> (s/split file #"\n")
       (map #(case %
               "A X" 3
               "A Y" 4
               "A Z" 8
               "B X" 1
               "B Y" 5
               "B Z" 9
               "C X" 2
               "C Y" 6
               "C Z" 7))
       (apply +)))

(comment
  (part-1)
  (part-2)
  )