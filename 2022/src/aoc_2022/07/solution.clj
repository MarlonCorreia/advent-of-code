(ns aoc-2022.07.solution
  (:require [clojure.string :as s]
            [clojure.core]))

(def file (slurp "src/aoc_2022/07/input.txt"))

(defn add-to-storage [size storage path]
  (let [size (-> size parse-long)]
    (loop [storage storage
           path path]
      (if (empty? path) storage
          (recur (assoc storage path (+ size (storage path 0)))
                 (pop path))))))

(defn build-storage [commands]
  (->> commands
       (reduce (fn [[s path] command] 
                 (let [[arg0 arg1 arg2] (s/split command #" ")]
                   (cond
                     (= arg1 "cd") (if (= arg2 "..")
                                     [s (pop path)]
                                     [s (conj path arg2)])
                     (not-empty (re-seq #"\d+" arg0)) 
                     (vector (add-to-storage arg0 s path) path)
                     :else [s path])))
               [{} []])
       first))

(defn part-1 []
  (->> (s/split-lines file)
       build-storage
       vals
       (filter #(<= % 100000))
       (apply +)))

(defn part-2 []
  (let [storage (->> (s/split-lines file) build-storage)
        used (- 70000000 (apply max (vals storage)))
        goal (- 30000000 used)]
    (->> (vals storage)
         (filter #(>= % goal))
         (apply min))))

(comment
  (part-1)
  (part-2))