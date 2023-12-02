(ns aoc-2023.01.solution
  (:require [clojure.string :as s]))

(def file (slurp "src/aoc_2023/01/input.txt"))

(def numbers {"one"   "1"
              "two"   "2"
              "three" "3"
              "four"  "4"
              "five"  "5"
              "six"   "6"
              "seven" "7"
              "eight" "8"
              "nine"  "9"})

(defn build-number-part-1 [line]
  (let [digits (->> line
                    (filter #(Character/isDigit %))
                    (apply str))]
    (parse-long (str (first digits) (last digits)))))

(defn get-index-of [number line]
  (loop [line line
         occ []
         idx 0]
    (if-let [pos (s/index-of line number idx)]
      (recur line (conj occ (vector (get numbers number) pos)) (+ pos (count number)))
      occ)))

(defn build-number-part-2 [line]
  (let [digits (keep-indexed (fn [pos i] (when (Character/isDigit i)
                                           (vector i pos))) line)
        n-digitis (->> (keys numbers)
                       (map #(get-index-of % line))
                       flatten
                       (partition 2))
        all-digits  (map first (sort-by second (concat digits n-digitis)))]
    (parse-long (str (first all-digits)
                     (last all-digits)))))

(defn part-1 []
  (->> file
       s/split-lines
       (map build-number-part-1)
       (apply +)))

(defn part-2 []
  (->> file
       s/split-lines
       (map build-number-part-2)
       (apply +)))