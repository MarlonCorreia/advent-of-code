(ns aoc-2022.04.solution
  (:require [clojure.string :as s]
            [clojure.set :as set]))

(def file (slurp "src/aoc_2022/04/input.txt"))

(defn parse-line [line]
  (let [x (s/replace line #"[,-]" " ")
        x (map parse-long (s/split x #" "))
        [x y] (partition-all 2 x)
        x (set (range (first x) (inc (second x))))
        y (set (range (first y) (inc (second y))))]
    (list x y)))

(defn is-subset? [line]
  (let [[x y] (parse-line line)]
    (or (set/subset? x y)
        (set/subset? y x))))

(defn intersect? [line]
  (let [[x y] (parse-line line)]
    (when (not-empty (set/intersection x y))
      true)))

(defn part-1 []
  (->> (s/split file #"\n")
       (map is-subset?)
       (filter true?)
       count))

(defn part-2 []
  (->> (s/split file #"\n")
       (map intersect?)
       (filter true?)
       count))

(comment
  (part-1)
  (part-2))
