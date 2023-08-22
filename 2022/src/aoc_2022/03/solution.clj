(ns aoc-2022.03.solution
  (:require [clojure.string :as s]
            [clojure.set :as set]))

(def file (slurp "src/aoc_2022/03/input.txt"))

(defn part-1 []
  (->> (s/split file #"\n")
       (map #(split-at (/ (count %) 2) %))
       (map (fn [[x y]]
              (set/intersection (set x) (set y)))) 
       (map #(if (<= (int \a) (int (first %)) (int \z))
               (- (int (first %)) 96)
               (- (int (first %)) 38)))
       (apply +)))


(defn part-2 []
  (loop [[x, y, z & remain] (s/split-lines file)
         final-sum 0]
    (if (empty? remain)
      (+ final-sum (let [c (first (set/intersection (set x) (set y) (set z)))]
                     (if (<= (int \a) (int c) (int \z))
                       (- (int c) 96)
                       (- (int c) 38))))
      (recur remain (+ final-sum (let [c (first (set/intersection (set x) (set y) (set z)))]
                                   (if (<= (int \a) (int c) (int \z))
                                     (- (int c) 96)
                                     (- (int c) 38))))))))

(comment
  (part-1)
  (part-2)
  )