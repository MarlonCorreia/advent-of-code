(ns aoc-2022.01.solution
  (:require [clojure.string :as s]))

(def file (slurp "src/aoc_2022/01/input.txt"))

(defn part-1 []
  (->> (s/split file #"\n\n")
       (map #(s/split % #"\n"))
       (map #(apply + (map (fn [x]
                         (Integer/parseInt x)) %)))
       (apply max)))

(defn part-2 []
  (->> (s/split file #"\n\n")
       (map #(s/split % #"\n"))
       (map #(apply + (map (fn [x]
                             (Integer/parseInt x)) %)))
       (sort)
       (reverse)
       (take 3)
       (apply +)))

(comment
  (part-1)
  (part-2)
  )